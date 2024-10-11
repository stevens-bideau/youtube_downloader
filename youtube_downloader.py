# Package : pip install yt-dlp

import yt_dlp

yt_url = input("Quelle est l'adresse url youtube de la vidéo ? ")
dest_name = input("Quel est le nom du fichier destination (sans l'extension .mp4) ? ")

url = yt_url
SAVE_PATH = 'C:/Users/steve/Downloads'

ydl_opts = {
    'format': 'best',
    'outtmpl': f'{SAVE_PATH}/{dest_name}.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# Exemple d'URL : 'https://www.youtube.com/watch?v=8tlN_y-QnFE'
