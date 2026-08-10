#!/usr/bin/env python3
"""
Gera delivery360-standalone.html: a página inteira num arquivo só.

Por que existe: o index.html usa caminhos absolutos (/assets/...), então só funciona
servido a partir da raiz de um domínio. Esta versão embute fontes, logos, ícone e JS
dentro do próprio HTML — abre com dois cliques, de qualquer pasta, sem servidor e
sem internet. Serve para testar, mandar por WhatsApp/e-mail e revisar offline.

O arquivo de produção continua sendo o index.html + /assets. Este aqui é derivado:
edite o index.html e rode este script de novo.

    python3 build-standalone.py

As fontes em base64 ficam num <style> separado no fim do <head>, marcado com um
comentário — assim o CSS legível não fica soterrado por 70KB de base64 se você
abrir o arquivo no bloco de notas.
"""

import base64
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).parent
ORIGEM = RAIZ / "index.html"
DESTINO = RAIZ / "delivery360-standalone.html"


def b64(caminho: pathlib.Path) -> str:
    return base64.b64encode(caminho.read_bytes()).decode("ascii")


def data_uri(caminho_relativo: str, mime: str) -> str:
    arquivo = RAIZ / caminho_relativo.lstrip("/")
    if not arquivo.exists():
        sys.exit(f"ERRO: asset nao encontrado: {arquivo}")
    return f"data:{mime};base64,{b64(arquivo)}"


def main() -> None:
    html = ORIGEM.read_text(encoding="utf-8")

    # ------------------------------------------------------------------ fontes
    fontes = {
        "/assets/fonts/anton-latin-400.woff2": "Anton",
        "/assets/fonts/archivo-latin-var.woff2": "Archivo",
    }
    blocos_font_face = re.findall(r"@font-face\{.*?\}\n", html, flags=re.S)
    if len(blocos_font_face) != 2:
        sys.exit(f"ERRO: esperava 2 blocos @font-face, achei {len(blocos_font_face)}")

    css_fontes = ""
    for bloco in blocos_font_face:
        novo = bloco
        for caminho in fontes:
            novo = novo.replace(caminho, data_uri(caminho, "font/woff2"))
        css_fontes += novo
        html = html.replace(bloco, "", 1)

    # tira os preload (os arquivos nao existem mais separados)
    html = re.sub(r'\s*<link rel="preload" href="/assets/fonts/[^>]*>', "", html)

    # ------------------------------------------------------- imagens e favicon
    html = html.replace(
        "/assets/img/logo-horizontal-cream.svg",
        data_uri("/assets/img/logo-horizontal-cream.svg", "image/svg+xml"),
    )
    html = html.replace(
        '<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">',
        f'<link rel="icon" href="{data_uri("/assets/img/favicon.svg", "image/svg+xml")}" type="image/svg+xml">',
    )
    # arquivos que so fazem sentido servidos por um dominio
    html = re.sub(r'\s*<link rel="apple-touch-icon"[^>]*>', "", html)
    html = re.sub(r'\s*<link rel="manifest"[^>]*>', "", html)

    # ----------------------------------------------------------- JavaScript
    js = (RAIZ / "assets/js/app.js").read_text(encoding="utf-8")
    html = html.replace(
        '<script src="/assets/js/app.js" type="module"></script>',
        "<script type=\"module\">\n" + js + "\n</script>",
    )

    # ------------------------------------------------------------------- CSP
    # Em file:// a origem e opaca, entao 'self' nao resolve e bloquearia tudo.
    # img-src precisa aceitar file: porque as fotos ficam soltas na pasta fotos/,
    # ao lado do HTML — elas nao sao embutidas (sao arquivos do cliente).
    # A politica segue fechada: sem rede, sem iframe, sem formulario.
    html = re.sub(
        r'<meta http-equiv="Content-Security-Policy"[^>]*>',
        '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; '
        "img-src 'self' data: file: blob:; font-src data:; style-src 'unsafe-inline'; "
        "script-src 'unsafe-inline'; base-uri 'none'; form-action 'none'\">",
        html,
    )

    # ----------------------------------------- fontes no fim do head + aviso
    aviso = (
        "\n<!--\n"
        "  ARQUIVO UNICO - Delivery 360 (Rodrigo Barros)\n"
        "  Gerado por build-standalone.py a partir de index.html.\n"
        "  Abre com dois cliques, sem servidor e sem internet.\n"
        "  Nao edite este arquivo: edite o index.html e rode o script de novo.\n"
        "-->\n"
    )
    html = html.replace("<!doctype html>", "<!doctype html>" + aviso, 1)

    html = html.replace(
        "</head>",
        "<style>\n"
        "/* ===================================================================\n"
        "   FONTES EMBUTIDAS EM BASE64 (Anton + Archivo).\n"
        "   Sao ~70KB de texto codificado. Pode rolar direto ate o fim do bloco:\n"
        "   nao ha nada editavel aqui.\n"
        "   (Nunca escreva a tag de fechamento de style dentro deste comentario:\n"
        "    o parser HTML encerra o bloco ali mesmo e o base64 vaza como texto.)\n"
        "   =================================================================== */\n"
        + css_fontes
        + "</style>\n</head>",
        1,
    )

    # ------------------------------------------------- verificacoes de sanidade
    corpo = html.split("<body", 1)[1]
    for tag in ("style", "script"):
        abre, fecha = corpo.count(f"<{tag}"), corpo.count(f"</{tag}>")
        if abre != fecha:
            sys.exit(f"ERRO: <{tag}> desbalanceado no body ({abre} x {fecha})")
    if "</style>" in css_fontes:
        sys.exit("ERRO: o CSS das fontes contem uma tag de fechamento de style")

    DESTINO.write_text(html, encoding="utf-8")

    kb = DESTINO.stat().st_size / 1024
    restantes = re.findall(r'(?:src|href)="(/assets/[^"]+)"', html)
    fotos = sorted(set(re.findall(r'src="(fotos/[^"]+)"', html)))
    print(f"gerado: {DESTINO.name}  ({kb:.0f} KB)")
    print("referencias a /assets restantes:", set(restantes) or "nenhuma")
    print("\nfotos do cliente (NAO embutidas — devem ficar ao lado do HTML):")
    for f in fotos:
        existe = "ok" if (RAIZ / f).exists() else "FALTANDO"
        print(f"  {f:34s} {existe}")


if __name__ == "__main__":
    main()
