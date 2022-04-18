import pytube

video = pytube.YouTube("https://www.youtube.com/watch?v=gK2yI-9kvgU&list=RDgK2yI-9kvgU&start_radio=1")
print(video.video_id)
print(pytube.YouTube(f"http://youtu.be/{video.video_id}").title)