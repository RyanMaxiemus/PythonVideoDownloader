"""
A simple GUI application to download YouTube videos using Pytube.

This script uses Tkinter for the GUI and Pytube for downloading videos.

Author: Ryan Maxie
Date: 2023-10-01
Version: 1.0
License: MIT License

Requirements:
    - pytube (pip install pytube)
"""

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
                     command=lambda: download())
btn.pack()

# Status label that will be updated after download
status_label = tkinter.Label(root, text="", font="arial 15")
status_label.pack(pady=5)


def download():
    """Captures the link from the entry, downloads the highest quality stream, and updates the status label."""
    try:
        # This captures the link(url) and locates it from YouTube.
        url = YouTube(str(link.get()))

        # This captures the streams available and gets the highest resolution.
        video = url.streams.get_highest_resolution()

        # This is the method with the instruction to download the video.
        video.download()

        # Update the status label on success
        status_label.config(text="Downloaded Successfully!", fg="green")
    except Exception as e:
        # Update the status label on error
        status_label.config(text=f"Error: {e}", fg="red")

root.mainloop()
