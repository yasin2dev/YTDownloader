import webbrowser
from tkinter import *
from tkinter.messagebox import showinfo

def popupBehaviour():
    pw = Toplevel()
    pw.wm_title("Behaviour of Program")
    pw.resizable(False, False)
    pw.geometry()

    lb = Label(pw, text="If YTDownloader is not responding after click download button, please wait until response. (Probably video downloading)")
    lb.pack(pady=20, padx=20)

    closeBtn = Button(pw, text="Close", command=pw.destroy)
    closeBtn.pack(pady=20, padx=20)

def ReportBug():
    webbrowser.open('mailto:yasin2developer@gmail.com', new=1)
