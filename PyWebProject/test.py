import pytube

try:
    video = pytube.YouTube("https://www.youtube.com/watch?v=gK2yI-9kvgU&list=RDgK2yI-9kvgU&start_radio=1")
    print(video.title)
except Exception:
    print('No such video existing')