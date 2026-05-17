from services.audio import baixar_midia
import os


def audio_para_texto(url: str):
    try:
        import whisper
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            "The whisper package is required for audio transcription. "
            "Install openai-whisper in requirements.txt or your environment."
        ) from e

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
