#!/usr/bin/env python3
"""
Gera fallback de cor para navegador antigo.

color-mix() só existe a partir do Chrome 111 e do Safari 16.2. Um PC preso no
Windows 7/8.1 trava no Chrome 109: toda declaração com color-mix() é descartada
e a página perde bordas, cores de apoio e brilhos.

O script resolve cada color-mix() para o rgba() equivalente e escreve a versão
literal ANTES da moderna:

    border:1px solid rgba(246,243,236,.14)/*!f*/;
    border:1px solid color-mix(in srgb,var(--cream) 14%,transparent);

O navegador antigo não entende a segunda linha, descarta e fica com a primeira.
O moderno entende as duas e a última vence. Nenhum pixel muda em navegador
atual — o build verifica isso comparando screenshot antes e depois.

    python3 compat-fallbacks.py            # aplica em index.html
    python3 compat-fallbacks.py --check    # só relata, não escreve

Rode de novo depois de mexer no CSS: as marcas /*!f*/ são removidas e
regeradas, então o script é idempotente.
"""

import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).parent
ALVO = RAIZ / "index.html"
MARCA = "/*!f*/"

NOMEADAS = {
    "transparent": (0, 0, 0, 0.0),
    "white": (255, 255, 255, 1.0),
    "black": (0, 0, 0, 1.0),
}


# --------------------------------------------------------------------------
# Leitura de cor
# --------------------------------------------------------------------------
def le_cor(txt: str, props: dict) -> tuple | None:
    """Devolve (r,g,b,a) ou None se não for uma cor que a gente saiba resolver."""
    t = txt.strip()
    if not t:
        return None

    baixo = t.lower()
    if baixo in NOMEADAS:
        return NOMEADAS[baixo]

    if t.startswith("#"):
        h = t[1:]
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 6:
            return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 1.0)
        if len(h) == 8:
            return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16) / 255)
        return None

    if baixo.startswith("var("):
        dentro = t[4:-1]
        # var(--x, fallback): tenta o nome, depois o fallback
        nome, _, alternativa = dentro.partition(",")
        val = props.get(nome.strip())
        if val is not None:
            return le_cor(val, props)
        return le_cor(alternativa, props) if alternativa.strip() else None

    if baixo.startswith("color-mix("):
        return resolve_mix(t, props)

    m = re.fullmatch(r"rgba?\((.*)\)", t, re.S | re.I)
    if m:
        corpo = m.group(1).replace("/", " ").replace(",", " ")
        partes = corpo.split()
        if len(partes) < 3:
            return None
        try:
            canais = [float(p.rstrip("%")) * (2.55 if p.endswith("%") else 1) for p in partes[:3]]
        except ValueError:
            return None
        alfa = 1.0
        if len(partes) > 3:
            p = partes[3]
            try:
                alfa = float(p.rstrip("%")) / (100 if p.endswith("%") else 1)
            except ValueError:
                return None
        return (canais[0], canais[1], canais[2], alfa)

    return None


def separa_topo(txt: str) -> list:
    """Quebra por vírgula respeitando parênteses aninhados."""
    partes, atual, prof = [], [], 0
    for ch in txt:
        if ch == "(":
            prof += 1
        elif ch == ")":
            prof -= 1
        if ch == "," and prof == 0:
            partes.append("".join(atual))
            atual = []
        else:
            atual.append(ch)
    partes.append("".join(atual))
    return partes


def resolve_mix(txt: str, props: dict) -> tuple | None:
    """color-mix(in srgb, A p%, B q%) -> (r,g,b,a), mistura com alfa pré-multiplicado."""
    dentro = txt[txt.index("(") + 1 : txt.rindex(")")]
    args = separa_topo(dentro)
    if len(args) != 3 or "srgb" not in args[0].lower():
        return None  # outro espaço de cor: não arrisca, deixa sem fallback

    def cor_e_peso(arg):
        arg = arg.strip()
        m = re.search(r"\s([\d.]+)%\s*$", " " + arg)
        peso = None
        if m:
            peso = float(m.group(1)) / 100
            arg = arg[: arg.rindex(m.group(1))].rstrip().rstrip("%").rstrip()
            arg = re.sub(r"[\d.]+%?\s*$", "", arg).strip() or arg
        return le_cor(arg, props), peso

    # o regex acima é frágil com "var(--x) 14%": refaz de forma explícita
    def parte(arg):
        arg = arg.strip()
        m = re.match(r"^(.*?)\s+([\d.]+)%$", arg, re.S)
        if m:
            return le_cor(m.group(1), props), float(m.group(2)) / 100
        return le_cor(arg, props), None

    c1, p1 = parte(args[1])
    c2, p2 = parte(args[2])
    if c1 is None or c2 is None:
        return None

    if p1 is None and p2 is None:
        p1 = p2 = 0.5
    elif p1 is None:
        p1 = 1 - p2
    elif p2 is None:
        p2 = 1 - p1
    soma = p1 + p2
    if soma == 0:
        return None
    p1, p2 = p1 / soma, p2 / soma

    a = c1[3] * p1 + c2[3] * p2
    if a == 0:
        return (0, 0, 0, 0.0)
    canais = [(c1[i] * c1[3] * p1 + c2[i] * c2[3] * p2) / a for i in range(3)]
    return (canais[0], canais[1], canais[2], a)


def escreve_cor(c: tuple) -> str:
    r, g, b = (max(0, min(255, round(c[i]))) for i in range(3))
    a = c[3]
    if a >= 0.999:
        return f"#{r:02x}{g:02x}{b:02x}"
    txt = f"{a:.3f}".rstrip("0").rstrip(".")
    return f"rgba({r},{g},{b},{txt or '0'})"


# --------------------------------------------------------------------------
# Varredura do CSS
# --------------------------------------------------------------------------
def acha_mixes(valor: str) -> list:
    """Posições (ini, fim) de cada color-mix( ... ) com parênteses equilibrados."""
    achados, i = [], 0
    while True:
        i = valor.find("color-mix(", i)
        if i < 0:
            return achados
        prof, j = 0, i + len("color-mix(") - 1
        while j < len(valor):
            if valor[j] == "(":
                prof += 1
            elif valor[j] == ")":
                prof -= 1
                if prof == 0:
                    break
            j += 1
        if prof != 0:
            return achados
        achados.append((i, j + 1))
        i = j + 1


def coleta_props(css: str) -> dict:
    """Custom properties declaradas no CSS. Última definição vence."""
    props = {}
    for m in re.finditer(r"(--[\w-]+)\s*:\s*([^;{}]+)", css):
        props[m.group(1)] = m.group(2).strip()
    return props


def transforma(css: str, props: dict, relatorio: list) -> str:
    saida, i, n = [], 0, len(css)
    profundidade, decl_ini = 0, None

    def despeja_decl(texto: str):
        bruto = texto.strip()
        if not bruto or ":" not in bruto:
            saida.append(texto)
            return
        mixes = acha_mixes(bruto)
        if not mixes:
            saida.append(texto)
            return
        literal, ok = [], True
        pos = 0
        for ini, fim in mixes:
            c = resolve_mix(bruto[ini:fim], props)
            if c is None:
                ok = False
                break
            literal.append(bruto[pos:ini])
            literal.append(escreve_cor(c))
            pos = fim
        if not ok:
            relatorio.append(("nao-resolvido", bruto[:90]))
            saida.append(texto)
            return
        literal.append(bruto[pos:])
        recuo = texto[: len(texto) - len(texto.lstrip())]
        saida.append(f"{recuo}{''.join(literal)}{MARCA};{texto.lstrip()}")
        relatorio.append(("ok", bruto.split(":")[0].strip()))

    while i < n:
        ch = css[i]
        if css.startswith("/*", i):
            fim = css.find("*/", i + 2)
            fim = n if fim < 0 else fim + 2
            trecho = css[i:fim]
            if decl_ini is None:
                saida.append(trecho)
            i = fim
            continue
        if ch == "{":
            if decl_ini is not None:
                saida.append(css[decl_ini:i])
                decl_ini = None
            saida.append(ch)
            profundidade += 1
            i += 1
            continue
        if ch == "}":
            if decl_ini is not None:
                despeja_decl(css[decl_ini:i])
                decl_ini = None
            saida.append(ch)
            profundidade -= 1
            i += 1
            continue
        if ch == ";" and profundidade > 0:
            if decl_ini is not None:
                despeja_decl(css[decl_ini:i])
                decl_ini = None
            saida.append(ch)
            i += 1
            continue
        if profundidade > 0:
            if decl_ini is None:
                decl_ini = i
            i += 1
            continue
        saida.append(ch)
        i += 1

    if decl_ini is not None:
        saida.append(css[decl_ini:])
    return "".join(saida)


def main() -> None:
    conferir = "--check" in sys.argv
    html = ALVO.read_text(encoding="utf-8")

    blocos = list(re.finditer(r"<style>(.*?)</style>", html, re.S))
    if not blocos:
        sys.exit("ERRO: nenhum bloco <style> em index.html")

    total = []
    novo = html
    for bloco in reversed(blocos):
        css = bloco.group(1)
        # limpa fallbacks de execuções anteriores para poder rodar de novo
        css = re.sub(r"[^;{}]*" + re.escape(MARCA) + r";", "", css)
        props = coleta_props(css)
        relatorio = []
        css = transforma(css, props, relatorio)
        total += relatorio
        novo = novo[: bloco.start(1)] + css + novo[bloco.end(1) :]

    ok = sum(1 for t, _ in total if t == "ok")
    falhas = [d for t, d in total if t != "ok"]
    print(f"declarações com color-mix: {ok + len(falhas)}")
    print(f"  fallback gerado: {ok}")
    print(f"  sem fallback:    {len(falhas)}")
    for f in falhas:
        print(f"    ! {f}")

    if conferir:
        return
    ALVO.write_text(novo, encoding="utf-8")
    print(f"gravado: {ALVO.name}")


if __name__ == "__main__":
    main()
