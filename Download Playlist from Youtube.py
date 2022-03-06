
from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME')

print(f'Downloading: {p.title}')
for video in p.videos:
    video.streams.get_highest_resolution().download()
    
