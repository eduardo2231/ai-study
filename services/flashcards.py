from PIL import Image, ImageDraw, ImageFont
import os
import textwrap
import shutil

from services.perguntas import organizando_texto

LARGURA = 800
ALTURA = 800

try:
    fonte = ImageFont.truetype("arial.ttf", 35)
except:
    fonte = ImageFont.load_default(size=35)


def criar_card(texto, cor_fundo, caminho):

    imagem = Image.new("RGB", (LARGURA, ALTURA), cor_fundo)

    draw = ImageDraw.Draw(imagem)

    linhas = textwrap.wrap(texto, width=20)

    texto_final = "\n".join(linhas)

    bbox = draw.multiline_textbbox(
        (0, 0),
        texto_final,
        font=fonte,
        align="center"
    )

    largura_texto = bbox[2] - bbox[0]
    altura_texto = bbox[3] - bbox[1]

    x = (LARGURA - largura_texto) / 2
    y = (ALTURA - altura_texto) / 2

    draw.multiline_text(
        (x, y),
        texto_final,
        fill="white",
        font=fonte,
        align="center"
    )

    imagem.save(caminho)


def gerar_flashcards(url=None, text=None):
    flashcards = organizando_texto(
        url=url,
        text=text
    )
    resetar_flashcards()

    for i, card in enumerate(flashcards):

        criar_card(
            texto=card["pergunta"],
            cor_fundo="blue",
            caminho=f"flashcards/{i}_pergunta.png"
        )

        criar_card(
            texto=card["resposta"],
            cor_fundo="red",
            caminho=f"flashcards/{i}_resposta.png"
        )

def resetar_flashcards(pasta="flashcards"):

    if os.path.exists(pasta):
        shutil.rmtree(pasta)

    os.makedirs(pasta, exist_ok=True)
