from pytube import YouTube #Import YouTube library
from sys import argv #Import command line argument library
import os #Import operating system library

#Check if command line argument is provided, ask user to provide link if not
if len(argv) < 2:
    print("Please provide a YouTube link as a command line argument in quotes.")
    exit(1)

link = argv[1] #Get YouTube link from command line

#Check if link is valid
try:
    yt = YouTube(link)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

#Print video information
print("Title: " + yt.title) #Get Video Title
print("Views: " + str(yt.views)) #Get Video Views

#Download Yotube Video to directory
yd = yt.streams.get_highest_resolution() #Get highest resolution video

#Set download path
download_path = "/Users/domingomesajr./Documents/Videos/YouTube Downloads"

#Check if directory exists
if not os.path.exists(download_path):
    print(f"The directory {download_path} does not exist.")
    exit(1)

#Try to download video
try:
    yd.download(download_path)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

#Print success message
print("DONE!")

exit(0) #Exit program
