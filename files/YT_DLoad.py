from pytube import YouTube
import os
import sys

PATH_SAVE = "F:\Downloads"
link = input("Enter Link: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Length: ", round(yt.length/60, 2))

print("Downloading...")

#Download Audio
audio_file = yt.streams.get_by_itag(140).download(PATH_SAVE)

base, ext = os.path.splitext(audio_file)
new_file = base + ".mp3"
os.rename(audio_file, new_file)

print("Download Complete!")

#Download Video
# ys = yt.streams.filter(res="1080p").first()
# ys.download(PATH_SAVE)