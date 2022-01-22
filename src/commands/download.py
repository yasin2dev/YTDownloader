from pytube import *
from tkinter import *
import pytube

def createConsole(master):
    global console
    console = Listbox(master, selectmode=SINGLE, width=50, height=20)
    console.pack(pady=50)

def DownloadWithHR(link):
    print(link)
    try:
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        video.download()
        console.insert(1, "Downloaded!")
    except pytube.exceptions.RegexMatchError:
        console.insert(1, "Wrong Link!")

def DownloadWithSelected(link, res):
    try:
        yt = YouTube(link)
        video = yt.streams.filter(res=res, file_extension='mp4').first()
        video.download()
        console.insert(1, "Downloaded!")
    except pytube.exceptions.RegexMatchError:
        console.insert(1, "Wrong Link!")
    except AttributeError:
        console.insert(1, "This video has not this resolution.")