from pytube import YouTube

link = "https://www.youtube.com/watch?v=g9FzOPtgRlc"

yt = YouTube(link)

try:
    yt.streams.filter(progressive = True,
file_extension = "mp4").first().download(filename="sample_video1")
except:
    print("Some Error!")
print('Task Completed!')

