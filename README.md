# PythonVideoDownloader

A simple GUI-based YouTube video downloader built with Python using Tkinter and PyTube.

**Author:** Ryan Maxie
**Version:** 1.0
**Date:** 2023-10-01
**License:** MIT License

## Features

- Clean, user-friendly GUI interface
- Download YouTube videos in highest available resolution
- Choose custom download location
- Real-time download status updates
- Threaded downloads to prevent UI freezing
- Error handling with informative messages

## Requirements

- Python 3.x
- pytube library (`pip install pytube`)
- tkinter (usually included with Python)

## Installation

1. Clone or download this repository
2. Install the required dependency:

   ```bash
   pip install pytube
   ```

## Usage

1. Run the application:

   ```bash
   python video_grabber.py
   ```

2. Paste a YouTube video URL into the input field
3. Click "Download Video"
4. Select a folder where you want to save the video
5. Wait for the download to complete

## How It Works

The application uses:

- **Tkinter** for the GUI interface (750x475 window)
- **PyTube** to fetch and download YouTube videos
- **Threading** to handle downloads without freezing the UI
- **filedialog** for folder selection

The core download logic in `_execute_download()` function:

1. Validates the YouTube URL
2. Fetches available video streams
3. Selects the highest resolution stream
4. Downloads to the specified path
5. Updates the status with success/error messages

## File Structure

- `video_grabber.py` - Main application file containing the GUI and download logic

## Error Handling

The application includes error handling for:

- Empty URL input
- Invalid YouTube URLs
- Download failures
- Network connectivity issues

Status messages are displayed in the GUI with color coding (green for success, red for errors, blue for in-progress).
