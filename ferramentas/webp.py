#!/usr/bin/env python3
"""
Converte imagens para WebP com as decisões que importam já embutidas.

  python3 ferramentas/webp.py fotos/aviao.png
  python3 ferramentas/webp.py fotos/*.png fotos/*.jpg
  python3 ferramentas/webp.py fotos/mariarita.jpg --largura 720

O original nunca é apagado. Se o WebP sair maior que o arquivo de origem,
o WebP é descartado e o motivo é informado — converter nem sempre vale a pena.

Requer: pip install Pillow
"""
import argparse
import os
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("Falta a Pillow. Rode:  pip install Pillow")


def kb(n):
    return "%.1f KB" % (n / 1024)


def tem_alfa(im):
    return im.mode in ("RGBA", "LA", "PA") or "transparency" in im.info


def poucas_cores(im, limite=512):
    """Arte chapada (logo, ícone) comprime melhor sem perdas.

    A contagem é feita na imagem inteira, sem reamostrar: reduzir a imagem
    antes de contar inventa cores intermediárias na interpolação e faz um
    logo de 4 cores parecer uma fotografia.
    """
    cores = im.convert("RGB").getcolors(maxcolors=limite)
    return cores is not None


def converter(caminho, largura_max=None, qualidade=82, forcar=None, apagar_maior=True):
    if not os.path.isfile(caminho):
        print("  %-28s arquivo nao encontrado" % os.path.basename(caminho))
        return

    origem = os.path.getsize(caminho)
    im = Image.open(caminho)
    lado_original = im.size

    # 1) Redimensiona antes de comprimir: economia de peso vem daqui, não da qualidade.
    if largura_max and im.width > largura_max:
        altura = round(im.height * largura_max / im.width)
        im = im.resize((largura_max, altura), Image.LANCZOS)

    # 2) Arte chapada vai sem perdas; foto vai com perdas.
    sem_perdas = forcar == "lossless" or (forcar is None and poucas_cores(im))

    # 3) Descarta EXIF, GPS e perfis — menos peso e nenhum metadado de câmera vazando.
    limpa = im.copy()
    limpa.info = {}
    if not tem_alfa(im) and limpa.mode != "RGB":
        limpa = limpa.convert("RGB")

    destino = os.path.splitext(caminho)[0] + ".webp"
    opcoes = {"method": 6}  # 6 = mais lento, menor arquivo
    if sem_perdas:
        opcoes["lossless"] = True
    else:
        opcoes["quality"] = qualidade
    limpa.save(destino, "WEBP", **opcoes)

    novo = os.path.getsize(destino)
    modo = "sem perdas" if sem_perdas else ("q%d" % qualidade)
    dim = "%dx%d" % lado_original
    if im.size != lado_original:
        dim += " -> %dx%d" % im.size

    if novo >= origem and apagar_maior:
        os.remove(destino)
        print("  %-28s %-19s %s -> %s  DESCARTADO (ficou maior)"
              % (os.path.basename(caminho), dim, kb(origem), kb(novo)))
        return

    ganho = (1 - novo / origem) * 100
    print("  %-28s %-19s %-9s %s -> %s  (-%.0f%%)"
          % (os.path.basename(caminho), dim, modo, kb(origem), kb(novo), ganho))


def main():
    p = argparse.ArgumentParser(description="Converte imagens para WebP.")
    p.add_argument("arquivos", nargs="+")
    p.add_argument("--largura", type=int, default=None,
                   help="largura maxima em px (redimensiona antes de comprimir)")
    p.add_argument("--q", type=int, default=82, help="qualidade 1-100 (padrao 82)")
    p.add_argument("--modo", choices=["lossless", "lossy"], default=None,
                   help="forca o modo; sem isso, decide pelo conteudo")
    p.add_argument("--manter-maiores", action="store_true",
                   help="mantem o .webp mesmo quando ele fica maior que o original")
    a = p.parse_args()

    print("  %-28s %-19s %-9s %s" % ("arquivo", "dimensoes", "modo", "peso"))
    print("  " + "-" * 76)
    for f in a.arquivos:
        converter(f, a.largura, a.q, a.modo, not a.manter_maiores)


if __name__ == "__main__":
    main()
