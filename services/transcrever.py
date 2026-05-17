import whisper
from services.audio import baixar_midia
import os

def audio_para_texto(url: str):

    arquivo = baixar_midia(url)

    if not arquivo:
        print("Erro: arquivo não foi baixado")
        return

    if not os.path.exists(arquivo):
        print(f"Erro: arquivo não existe -> {arquivo}")
        return

    model = whisper.load_model("base")

    try:
        resultado = model.transcribe(arquivo)
        print(resultado["text"])
        return resultado["text"], arquivo
    except Exception as e:
        print("Erro no Whisper:", e)
