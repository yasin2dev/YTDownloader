#YTDownloader v0.1

from tkinter import *
import ctypes
import commands.download, commands.menuCommands

#For the high resolution rendering
ctypes.windll.shcore.SetProcessDpiAwareness(True)

class App(Tk):
    def __init__(self, master=None):
        super().__init__(master)

        self.title("YTDownloader")
        self.resizable(False,False)
        self.geometry("480x640")

        self.lb = Label(self, text="YTDownloader", font='Arial')
        self.lb.pack(pady=10)

        self.mainMenu = Menu(self.master)
        self.helpMenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Help", menu=self.helpMenu)
        #TODO menuCommands@16
        self.helpMenu.add_command(label="Report a Bug")
        self.helpMenu.add_command(label="Behaviour of YT", command=commands.menuCommands.popupBehaviour)

        self.config(menu=self.mainMenu)

        self.Components()

    def Components(self):
        #YouTube Link info label
        self.labelText = Label(self.master, text="Enter Youtube Link: ")
        self.labelText.pack()

        #YouTube Link Entry
        self.ytLink = Entry(self.master, width=50)
        self.ytLink.pack(pady=10)

        #Option Menu of Select resolution
        self.value_i = StringVar(self.master)
        self.value_i.set("Select Video Resolution")
        self.option_t = ("Highest", "144p", "240p", "360p", "480p", "720p", "1080p")
        self.option_m = OptionMenu(self.master,  self.value_i, *self.option_t)
        self.option_m.pack(pady=15)

        #Download Button - Command is running DownloadOperations function.
        self.downloadBtn = Button(self.master, text="Download", command=self.DownloadOperations)
        self.downloadBtn.pack()

        commands.download.createConsole(self.master)

    def DownloadOperations(self):
        if self.option_t[0] == self.value_i.get():
           commands.download.DownloadWithHR(self.ytLink.get())
        else:
            commands.download.DownloadWithSelected(self.ytLink.get(), self.value_i.get())



if __name__ == "__main__":
    app = App()
    app.mainloop()