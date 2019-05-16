import pytube
print("Enter the URL")
link = input()
yt = pytube.YouTube(link)
stream = yt.streams.first()
print("Enter Destination ")
dest=input()
stream.download(dest)
print("Video Downloaded Successfully!")
