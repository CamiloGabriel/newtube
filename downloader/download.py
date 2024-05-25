import os
import logging
from pytube import YouTube
from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def baixar_video(url,caminho_destino='videos'):
    try:
        yt = YouTube(url)
        video_stream = yt.stream.get_highest_resolution()

        if not os.path.exists(caminho_destino):
            os.makedirs(caminho_destino)

        logging.info(f'Baixando {yt.title}...')
        video_stream.download(caminho_destino)
        logging.info(f'{yt.title} download concluído!')
    except Exception as e:
        logging.error(f'Erro ao baixar o vídeo {url}: {e}')
        raise

def baixar_videos(urls,caminho_destino='videos'):
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(baixar_video,url,caminho_destino) for url in urls]
        for future in futures:
            try:
                future.result()
            except Exception as e:
                logging.error(f'Erro ao baixar o vídeo: {e}')
