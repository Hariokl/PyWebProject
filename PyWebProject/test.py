import pytube

video = pytube.YouTube("https://www.youtube.com/watch?v=k1BneeJTDcU&list=RDYy310SQmlbM&index=5")
st = video.streams.filter(only_video=True)
print(st)