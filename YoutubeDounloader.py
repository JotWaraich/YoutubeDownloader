from pytube import YouTube
from sys import argv

# link = input("Enter link : ")
link = argv[1]
yt = YouTube(link)

print("tital :", yt.title)
print("views :", yt.views)

yd = yt.streams.get_highest_resolution() #for the highest resolution
# yd = yt.streams.get_by_resolution(1080)
path = input("Enter path : ")
yd.download(path)