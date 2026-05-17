import re
from groq import Groq
from services.transcrever import audio_para_texto
import streamlit as st
import os

def gerar_perguntas(url=None, text=None, api=st.secrets["GROQ_API_KEY"]) -> str:
    if url:
        texto, arquivo = audio_para_texto(url)
    else:
        texto = text
        arquivo = None

    prompt = f"""
    Based on the text below, generate multiple question-and-answer blocks according with language of text
    if portugues generate in portuguese if english generate in english.

    The questions and answers MUST be based only on the provided text.

    TEXT:
    {texto}

    You MUST respond only using the exact format below.

    Do not add explanations.
    Do not use markdown.
    Do not number items.
    Do not write anything outside the required structure.

    Required format:

    [START]
    R: question
    Q: answer
    [END]

    Rules:
    - Always generate one question followed by one answer
    - Questions must be based on the provided text
    - Answers must be derived from the provided text
    - Keep answers concise and clear
    - Preserve the exact tags: [START] and [END]
    - Preserve the exact prefixes: "R:" and "Q:"
    - Separate each block with a blank line
    """

    client = Groq(api_key=api)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
        )

    if arquivo and os.path.exists(arquivo):
        os.remove(arquivo)

    return response.choices[0].message.content

def organizando_texto(url=None, text=None):
    texto = gerar_perguntas(url=url,text=text)
    pattern = r"\[START\]\s*R:\s*(.*?)\s*Q:\s*(.*?)\s*\[END\]"
    matches = re.findall(pattern, texto, re.DOTALL)

    dados = []

    for pergunta, resposta in matches:
        dados.append({
            "pergunta": pergunta.strip(),
            "resposta": resposta.strip()
        })

    return dados

# "https://www.youtube.com/watch?v=lDrKIqubzdw"