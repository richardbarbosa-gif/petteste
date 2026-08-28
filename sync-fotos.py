#!/usr/bin/env python3
"""
Lê as dimensões reais dos arquivos em fotos/ e injeta width/height nas <img>
correspondentes do index.html.

Por que existe: imagem sem width/height faz a página "pular" enquanto carrega
(Cumulative Layout Shift), e o Google usa isso no ranking. Como as fotos são
trocadas pelo cliente, deixar os números fixos no HTML quebraria na primeira
substituição — este script mantém tudo sincronizado com o arquivo que está lá.

    python3 sync-fotos.py

Roda sozinho e também é chamado por build-standalone.py. Só usa a biblioteca
padrão do Python: lê o cabeçalho do PNG/JPEG/GIF/WEBP na mão, sem instalar nada.
"""

import pathlib
import re
import struct
import sys

RAIZ = pathlib.Path(__file__).parent
ALVO = RAIZ / "index.html"


def dimensoes(caminho: pathlib.Path):
    """Devolve (largura, altura) lendo só o cabeçalho do arquivo."""
    with open(caminho, "rb") as f:
        cab = f.read(32)

        # PNG: IHDR vem logo após a assinatura de 8 bytes
        if cab[:8] == b"\x89PNG\r\n\x1a\n":
            return struct.unpack(">II", cab[16:24])

        # GIF: little-endian, logo após "GIF87a"/"GIF89a"
        if cab[:6] in (b"GIF87a", b"GIF89a"):
            return struct.unpack("<HH", cab[6:10])

        # WEBP (VP8X / VP8L / VP8 simples)
        if cab[:4] == b"RIFF" and cab[8:12] == b"WEBP":
            f.seek(12)
            bloco = f.read(14)
            if bloco[:4] == b"VP8X":
                w = int.from_bytes(bloco[8:11], "little") + 1
                h = int.from_bytes(bloco[11:14], "little") + 1
                return w, h
            f.seek(26)
            d = f.read(4)
            if len(d) == 4:
                return struct.unpack("<HH", d)

        # JPEG: percorre os marcadores até achar um SOF
        if cab[:2] == b"\xff\xd8":
            f.seek(2)
            while True:
                b = f.read(1)
                if not b:
                    break
                if b != b"\xff":
                    continue
                while b == b"\xff":
                    b = f.read(1)
                marcador = b[0]
                if marcador in (0xD8, 0xD9) or 0xD0 <= marcador <= 0xD7:
                    continue
                dados = f.read(2)
                if len(dados) < 2:
                    break
                tam = struct.unpack(">H", dados)[0]
                # SOF0..SOF15, exceto DHT(C4), JPG(C8) e DAC(CC)
                if 0xC0 <= marcador <= 0xCF and marcador not in (0xC4, 0xC8, 0xCC):
                    corpo = f.read(5)
                    if len(corpo) == 5:
                        alt, larg = struct.unpack(">HH", corpo[1:5])
                        return larg, alt
                    break
                f.seek(tam - 2, 1)
    return None


def main() -> int:
    if not ALVO.exists():
        sys.exit("ERRO: index.html nao encontrado")

    html = ALVO.read_text(encoding="utf-8")
    referencias = sorted(set(re.findall(r'<img[^>]*\ssrc="(fotos/[^"]+)"', html)))
    if not referencias:
        print("nenhuma <img> apontando para fotos/ — nada a fazer")
        return 0

    alterados, faltando = 0, []
    for ref in referencias:
        arquivo = RAIZ / ref
        if not arquivo.exists():
            faltando.append(ref)
            continue
        dim = dimensoes(arquivo)
        if not dim:
            faltando.append(f"{ref} (formato nao reconhecido)")
            continue
        w, h = dim

        def repor(m, w=w, h=h):
            tag = m.group(0)
            tag = re.sub(r'\s(?:width|height)="\d+"', "", tag)
            return tag[:-1].rstrip() + f' width="{w}" height="{h}">'

        novo, n = re.subn(rf'<img[^>]*\ssrc="{re.escape(ref)}"[^>]*>', repor, html)
        if n:
            html, alterados = novo, alterados + n
        print(f"  {ref:26s} {w}x{h}")

    ALVO.write_text(html, encoding="utf-8")
    print(f"\n{alterados} tag(s) <img> sincronizada(s) com os arquivos reais")
    if faltando:
        print("AVISO — sem dimensao (a pagina vai 'pular' ao carregar):")
        for f in faltando:
            print("  -", f)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
