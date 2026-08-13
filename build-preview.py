#!/usr/bin/env python3
"""
Gera preview.html: a página empacotada para hospedagem de prévia.

Diferença para o build-standalone: aqui TODAS as imagens (inclusive as de
fotos/) entram em base64, porque o hospedeiro da prévia bloqueia qualquer
arquivo externo. E o arquivo sai sem <!doctype>, <html>, <head> e <body>,
porque o hospedeiro envolve o conteúdo no próprio esqueleto.

    python3 build-preview.py

A prévia é uma foto do momento. O que vai para o ar continua sendo o
index.html + /assets + fotos/.
"""

import base64
import mimetypes
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).parent
ORIGEM = RAIZ / "index.html"
DESTINO = RAIZ / "preview.html"


def data_uri(rel: str) -> str:
    arq = RAIZ / rel.lstrip("/")
    if not arq.exists():
        sys.exit(f"ERRO: asset nao encontrado: {arq}")
    mime = mimetypes.guess_type(arq.name)[0] or "application/octet-stream"
    if arq.suffix == ".woff2":
        mime = "font/woff2"
    return f"data:{mime};base64,{base64.b64encode(arq.read_bytes()).decode('ascii')}"


def main() -> None:
    html = ORIGEM.read_text(encoding="utf-8")

    # ---- fontes embutidas ----
    for caminho in (
        "/assets/fonts/anton-latin-400.woff2",
        "/assets/fonts/archivo-latin-var.woff2",
    ):
        html = html.replace(f"url('{caminho}')", f"url('{data_uri(caminho)}')")

    # ---- todas as imagens: logo + pasta fotos/ ----
    for ref in sorted(set(re.findall(r'(?:src|href)="((?:/assets/img|fotos)/[^"]+)"', html))):
        html = html.replace(f'"{ref}"', f'"{data_uri(ref)}"')

    # ---- JavaScript embutido, com guarda para o <dialog> ----
    js = (RAIZ / "assets/js/app.js").read_text(encoding="utf-8")
    js = js.replace("lb.showModal();", "try { lb.showModal(); } catch (e) { /* modal bloqueado no host */ }")
    html = html.replace(
        '<script src="/assets/js/app.js" type="module"></script>',
        '<script type="module">\n' + js + "\n</script>",
    )

    # ---- fora: o hospedeiro fornece o esqueleto e a própria política ----
    html = re.sub(r'\s*<meta http-equiv="Content-Security-Policy"[^>]*>', "", html)
    html = re.sub(r'\s*<link rel="(?:manifest|apple-touch-icon|icon|canonical|preload)"[^>]*>', "", html)
    html = re.sub(r"\s*<script type=\"application/ld\+json\">.*?</script>", "", html, flags=re.S)

    cabeca = html.split("<head>", 1)[1].split("</head>", 1)[0]
    corpo = html.split("<body>", 1)[1].split("</body>", 1)[0]

    titulo = re.search(r"<title>(.*?)</title>", cabeca, re.S)
    estilos = "\n".join(re.findall(r"<style>.*?</style>", cabeca, re.S))

    saida = (
        "<title>Delivery 360°</title>\n"
        f"<!-- Prévia gerada de index.html — {titulo.group(1) if titulo else ''} -->\n"
        + estilos
        + "\n"
        + corpo.strip()
        + "\n"
    )

    # \b evita falso positivo: <header> contem "<head"
    for proibida in (r"<!doctype", r"<html\b", r"<head\b", r"<body\b"):
        if re.search(proibida, saida, re.I):
            sys.exit(f"ERRO: {proibida} nao pode aparecer no arquivo de previa")
    if re.search(r"(?:src|href)=\"(?:/assets|fotos)/", saida):
        sys.exit("ERRO: sobrou referencia a arquivo externo — a previa nao carregaria")

    DESTINO.write_text(saida, encoding="utf-8")
    print(f"gerado: {DESTINO.name}  ({DESTINO.stat().st_size/1024/1024:.2f} MB)")
    print("referencias externas: nenhuma")


if __name__ == "__main__":
    main()
