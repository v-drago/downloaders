from pytube import YouTube

# Set this to your preferred path
path = "C:/Users/User/Music"

link = input("Enter YouTube URL: ")

video = YouTube(link)

stream = video.streams.get_audio_only("mp4")

print("Downloading...")

stream.download(path, f"{stream.title}.mp3")

print("Done")
