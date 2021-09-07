from pytube import YouTube


print("Enter URL of youtube video")
video = YouTube(input())

print(video.title)
print(video.streams.get_highest_resolution.__sizeof__())
video.streams.get_highest_resolution().download()
print('------------------------Your video has been downloaded------------------------')
print('--------Thank You----------')