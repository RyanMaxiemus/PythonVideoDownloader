"""
A simple GUI application to download YouTube videos using Pytube.

See README.md for detailed usage instructions and features.
"""

# Import necessary libraries.
import tkinter
import threading
from tkinter import filedialog

# Import the youtube library from the installed Pytube module.
from pytube import YouTube

# Create window.
root = tkinter.Tk()

# Create size of window.
root.geometry('750x475')

# Makes the window adjustable with its features.
root.resizable(height=None, width=None)
root.title('Video Downloader')

# Create a label for the title of the application.
lbl1 = tkinter.Label(root,
                     text="Download Videos",
                     font='san-serif 14 bold')
lbl1.pack(pady=10)

# Specifying the variable type
link = tkinter.StringVar()

# Label for the YouTube link input
lbl2 = tkinter.Label(root,
                     text="Gimme a link ya filthy animal!",
                     font='san-serif 15 bold')
lbl2.pack(pady=10)

# Entry widget for the YouTube link.
link_enter = tkinter.Entry(root, width=70, textvariable=link)
link_enter.pack(pady=10)

# Download button that triggers the download process
btn = tkinter.Button(root,
                     text='Download Video',
                     font='san-serif 16 bold',
                     bg='red',
                     padx=2,
                     command=lambda: download())

# Pack the button into the window.
btn.pack()

# Status label that will be updated after download
status_label = tkinter.Label(root, text="", font="arial 15")
status_label.pack(pady=5)

# Function to execute the download in a separate thread
def _execute_download(save_path: str):
    """Contains the core download logic to be run in a separate thread."""
    try:
        # This captures the link(url) and locates it on YouTube.
        yt_url = str(link.get())

        # Check if the URL is empty and raise funny error if s.
        if not yt_url:
            raise ValueError("Please enter your YouTube video's URL, ya dipshit!")
        url = YouTube(yt_url)

        # This captures the streams available and gets the highest resolution.
        video = url.streams.get_highest_resolution()

        # This is the method with the instruction to download the video.
        video.download(output_path=save_path)

        # Update the status label on success
        status_label.config(text=f"Holy shit, the download was successful! I thought for sure was about to get nuked,  I've left the vid in {save_path}.", fg="green")

    except Exception as e:
        # Update the status label on error.
        status_label.config(text=f"Error: {e}", fg="red", wraplength=500)

    finally:
        # Re-enable the download button.
        btn.config(state=tkinter.NORMAL)

def download():
    """Asks for a save location, then starts the download in a new thread."""
    save_path = filedialog.askdirectory()

    if not save_path:
        # User cancelled the dialog, so do nothing.
        return

    btn.config(state=tkinter.DISABLED)  # Disable button during download
    status_label.config(text="Downloading...", fg="blue")
    threading.Thread(target=_execute_download, args=(save_path,)).start()

root.mainloop()
