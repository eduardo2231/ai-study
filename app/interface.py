import streamlit as st
import os

from services.flashcards import gerar_flashcards
from services.flashcards import resetar_flashcards

def main():

    tab1, tab2 = st.tabs(["🖥 Url to Flashcards", "📙 Text to Flashcards"])

    if "mostrar_url" not in st.session_state:
        st.session_state.mostrar_url = False

    if "mostrar_texto" not in st.session_state:
        st.session_state.mostrar_texto = False

    if "indice_url" not in st.session_state:
        st.session_state.indice_url = 0

    if "indice_texto" not in st.session_state:
        st.session_state.indice_texto = 0

    with tab1:

        url = st.text_input("Coloque a Url:")

        if st.button("Gerar Flashcards URL"):

            if url.strip() == "":
                st.warning("Por favor, insira seu link.")

            else:
                with st.spinner("Gerando Flashcards..."):

                    try:
                        resetar_flashcards()
                        gerar_flashcards(url)

                        st.session_state.mostrar_url = True
                        st.session_state.indice_url = 0

                        st.success("Flashcards gerados!!")

                    except Exception as e:
                        st.error(e)

        if st.session_state.mostrar_url:
            mostrar_flashcards("url")

    with tab2:

        texto = st.text_area("Coloque seu texto:", height=500)

        if st.button("Gerar Flashcards Texto"):

            if texto.strip() == "":
                st.warning("Por favor, insira seu texto.")

            else:
                with st.spinner("Gerando Flashcards..."):

                    try:
                        resetar_flashcards()
                        gerar_flashcards(text=texto)

                        st.session_state.mostrar_texto = True
                        st.session_state.indice_texto = 0

                        st.success("Flashcards gerados!!")

                    except Exception as e:
                        st.error(e)

        if st.session_state.mostrar_texto:
            mostrar_flashcards("texto")


def mostrar_flashcards(tipo):

    pasta = "flashcards"

    imagens = sorted([
        img for img in os.listdir(pasta)
        if img.endswith(".png")
    ])

    if not imagens:
        return

    key_idx = "indice_url" if tipo == "url" else "indice_texto"

    st.image(
        os.path.join(pasta, imagens[st.session_state[key_idx]]),
        width=400
    )

    col1, col2 = st.columns(2)

    if col1.button("⬅", key=f"anterior_{tipo}"):

        st.session_state[key_idx] -= 1

        if st.session_state[key_idx] < 0:
            st.session_state[key_idx] = len(imagens) - 1

    if col2.button("➡", key=f"proximo_{tipo}"):

        st.session_state[key_idx] += 1

        if st.session_state[key_idx] >= len(imagens):
            st.session_state[key_idx] = 0