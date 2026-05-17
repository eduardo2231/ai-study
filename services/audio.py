import os
import yt_dlp

def baixar_midia(url: str, pasta_saida="downloads"):

    os.makedirs(pasta_saida, exist_ok=True)

    arquivo_final = None

    def hook(d):
        nonlocal arquivo_final
        if d["status"] == "finished":
            arquivo_final = d["filename"]

    opcoes = {
        "format": "bestaudio/best",
        "outtmpl": f"{pasta_saida}/%(title)s.%(ext)s",
        "restrictfilenames": True,
        "noplaylist": True,
        "quiet": False,
        "no_warnings": True,
        "retries": 3,
        "fragment_retries": 3,

        "progress_hooks": [hook],

        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:

            info = ydl.extract_info(url, download=True)

            arquivo_final = os.path.splitext(arquivo_final)[0] + ".mp3"

            print("\n========== INFO ==========")
            print(f"Título: {info.get('title')}")
            print(f"Canal: {info.get('uploader')}")
            print(f"Site: {info.get('extractor')}")
            print("==========================\n")

        print("Download concluído.")

        return arquivo_final

    except Exception as e:
        print(f"Erro: {e}")
        return None
