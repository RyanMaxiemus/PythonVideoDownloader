# Import Tkinter libraries from the module
import tkinter

# Import the youtube library from the installed Pytube module.
from pytube import YouTube

# Create window
root = tkinter.Tk()

# Size of window
root.geometry('750x475')

# Makes the window adjustable with its features
root.resizable(height=None, width=None)
root.title('Video Downloader')

lbl1 = tkinter.Label(root,
                     text="Download Videos",
                     font='san-serif 14 bold')
lbl1.pack(pady=10)

# Specifying the variable type
link = tkinter.StringVar()

lbl2 = tkinter.Label(root,
                     text="Paste your link here",
                     font='san-serif 15 bold')
lbl2.pack(pady=10)

link_enter = tkinter.Entry(root, width=70, textvariable=link)
link_enter.pack(pady=10)

btn = tkinter.Button(root,
                     text='Download Video',
                     font='san-serif 16 bold',
                     bg='red',
                     padx=2,
                     command="download")

btn.pack()


def download():
    # This captures the link(url) and locates it from YouTube.
    url = YouTube(str(link.get()))

    # This captures the streams available i.e. 360p, 720p, 1080p. etc.
    video = url.streams.first()

    # This is the method with the instruction to download the video.
    video.download()

    # Once the video is downloaded, the label `Downloaded` is displayed to show dowload completion.

    tkinter.Label(root,
                  text="Downloaded",
                  font="arial 15").place(x=100, y=120)


root.mainloop()
