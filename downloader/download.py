import os
from pytube import YouTube
from concurrent.futures import ThreadPoolExecutor

def baixar_video(url,caminho_destino='videos'):
    yt = YouTube(url)
    video_stream = yt.stream.get_highest_resolution()

    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino)
    
    print(f'Baixando {yt.title}...')
    video_stream.download(caminho_destino)
    print(f'{yt.title} Download conluído!')


def baixar_videos(urls,caminho_destino='videos'):
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(baixar_video,url,caminho_destino) for url in urls]
        for future in futures:
            future.result()