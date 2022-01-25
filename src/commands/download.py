import tkinter.filedialog

from pytube import *
from tkinter import *
import pytube

def SelectDownloadPath():
    filetypes = [('MP4 File', '*.mp4'), ('All Files', '*.*')]
    global file
    file = tkinter.filedialog.asksaveasfilename(filetypes=filetypes, defaultextension=filetypes)

def createConsole(master):
    global console
    console = Listbox(master, selectmode=SINGLE, width=50, height=20)
    console.pack(pady=50)

def DownloadWithHR(link):
    try:
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        if not file:
            return
        else:
            video.download(output_path=file)
            console.insert(1, "Downloaded!")
    except pytube.exceptions.RegexMatchError:
        console.insert(1, "Wrong Link!")

def DownloadWithSelected(link, res):
    try:
        yt = YouTube(link)
        video = yt.streams.filter(res=res, file_extension='mp4').first()
        if not file:
            return
        else:
            video.download(output_path=file)
            console.insert(1, "Downloaded!")
    except pytube.exceptions.RegexMatchError:
        console.insert(1, "Wrong Link!")
    except AttributeError:
        console.insert(1, "This video has not this resolution.")