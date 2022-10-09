from pytube import YouTube
import sys

urls = [

]

# def download(url):
#     try:
#         yt = YouTube(url)
#         yt.streams.filter(progressive = True, 
#     file_extension = "mp4").first().download(output_path = ".")
#     except:
#         sys.stderr.write("An Error Occured.")
#     print('Task Completed!')

def download(url):
    yt = YouTube(url)
    yt.streams.filter(progressive = True, 
    file_extension = "mp4").first().download(output_path = ".")
   
  

def runner():
    for url in urls:
        download(url)

if __name__ == "__main__":
    runner()


# if __name__ == "__main__":
#     download(sys.argv[1])
