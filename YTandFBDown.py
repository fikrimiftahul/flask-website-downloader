#Import the YoutubeDL module from the yt_dlp library
from yt_dlp import YoutubeDL

#Set the URL to download using the 'url' variable
url = 'Paste your url here'
ydl_opts = {'outtmpl': '%(title)s.%(ext)s', 'format': 'mp4'} #Set options for the download process in the 'ydl_opts' dictionary
with YoutubeDL (ydl_opts) as ydl: #Initialize a new instance of the YoutubeDL class with the 'ydl_opts' dictionary as an argument
    try:
        ydl.download([url])
    
    except Exception as e:
        print('Smething is wrong', e) ## Print an error message with the exception message if an exception occurs during the download process
