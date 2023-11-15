# ytdownload.py

This Python script allows you to download YouTube videos directly to your local machine. It uses the `pytube` library to access and download YouTube content.

## How it works

The script takes a YouTube link as a command-line argument. It then uses the `pytube` library to create a `YouTube` object with the provided link.

The script checks if the link is valid and if the video is accessible. If the link is invalid or the video is inaccessible, it will print an error message and exit.

If the link is valid, the script will print the title and the number of views of the video.

The script then downloads the video with the highest available resolution to a specified directory on your local machine.

## Usage

To use this script, run the following command in your terminal:

```bash
python3 ytdownload.py "your_youtube_link_here"
```

Replace `"your_youtube_link_here"` with the actual link to the YouTube video you want to download.

## Dependencies

This script requires the `pytube` library. You can install it using pip:

```bash
pip3 install pytube
```

Please note that the download path is currently hardcoded. You may need to modify the `download_path` variable in the script to match the directory where you want to save the videos.