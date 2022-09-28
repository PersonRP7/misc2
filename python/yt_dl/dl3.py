from pytube import YouTube
import sys


def download(url):
    try:
        yt = YouTube(url)
        yt.streams.filter(progressive = True, 
    file_extension = "mp4").first().download(output_path = ".")
    except:
        print("Some Error!")
    print('Task Completed!')

if __name__ == "__main__":
    download(sys.argv[1])