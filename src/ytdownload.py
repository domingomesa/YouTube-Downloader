import yt_dlp #Import YouTube library
import sys #Import command line argument library
import os #Import operating system library

def download_video(url, download_path):
    ydl_opts = {
        "outtmpl": os.path.join(download_path, "%(title)s.%(ext)s"),  # Set output template
        "format": "best",  # Download the best quality available
        "noplaylist": True,  # Download only the video, not the playlist
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            #Get video information
            info = ydl.extract_info(url, download=False)
            print(f"Title: {info.get('title', 'N/A')}")
            print(f"Views: {info.get('view_count', 'N/A')}")
            
            # Download the video
            ydl.download([url])
            print("DONE!")

        except Exception as e:
            print(f"An error occurred: {e}")
            return False

def main():
    #Check if command line argument is provided, ask user to provide link if not
    if len(sys.argv) < 2:
        print("Please provide a YouTube link as a command line argument in quotes.")
        sys.exit(1)

    url = sys.argv[1] #Get YouTube url from command line
    #Set download path
    download_path = sys.argv[2] if len(sys.argv) > 2 else os.getcwd() #Get download path from command line or use current working directory

    #Check if directory exists
    if not os.path.exists(download_path):
        print(f"The directory {download_path} does not exist.")
        sys.exit(1)

    success = download_video(url, download_path)

    sys.exit(0 if success else 1) #Exit program

if __name__ == "__main__":
    main()