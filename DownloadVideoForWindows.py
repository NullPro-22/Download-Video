from pafy import new
from os import system
system("cls")
video = input("Pleas Enter video url : ")
print("The Video is Downloading...")
print("")
v = new(video)
stream = v.streams
for i in stream:
	print(i)
	stream[0].download()
print("The Video is Download : ")
