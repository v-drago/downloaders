from pytube import YouTube

# Set this to your preferred path
path = "C:/Users/User/Videos"

link = input("Enter YouTube URL: ")

video = YouTube(link)

stream = video.streams.get_highest_resolution()

print("Downloading...")

stream.download(path)

print("Done")