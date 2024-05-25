from downloader.downloader import baixar_videos

if __name__ == '__main__':
    urls = input('Digite as URLs dos vídeos (separadas por vírgula): ').split(',')
    baixar_videos([url.strip() for url in urls])