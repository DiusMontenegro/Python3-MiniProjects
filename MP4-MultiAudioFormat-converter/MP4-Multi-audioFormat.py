import os
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *
from pydub import AudioSegment

# Set up GUI window
root = tk.Tk()
root.title("Video to Audio Converter")
root.geometry("500x200")

# Supported audio formats
AUDIO_FORMATS = [
    "mp3",
    "aac",
    "flac",
    "wav",
    "ogg",
    "wma"
]

# Function to open file dialog and get selected file
def browse_file():
    global filepath
    filepath = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])

# Function to convert video file to selected audio format
def convert_file():
    if filepath:
        # Get the file name and directory
        file_dir = os.path.dirname(filepath)
        file_name = os.path.splitext(os.path.basename(filepath))[0]

        # Get selected audio format
        selected_format = format_var.get()

        # Create audio file name
        audio_file = os.path.join(file_dir, file_name + "." + selected_format)

        # Use moviepy library to convert file
        video = VideoFileClip(filepath)
        audio = video.audio
        audio.write_audiofile(audio_file)

        # Convert to other formats using pydub
        for format in AUDIO_FORMATS:
            if format != selected_format:
                new_audio_file = os.path.join(file_dir, file_name + "." + format)
                AudioSegment.from_file(audio_file).export(new_audio_file, format=format)

        # Display success message
        message_label.config(text="Conversion successful. File saved as " + audio_file)

# Function to download converted audio file
def download_file():
    if filepath:
        # Get the file name and directory
        file_dir = os.path.dirname(filepath)
        file_name = os.path.splitext(os.path.basename(filepath))[0]

        # Get selected audio format
        selected_format = format_var.get()

        # Create audio file name
        audio_file = os.path.join(file_dir, file_name + "." + selected_format)

        # Set up download options
        root.filename = file_name + "." + selected_format
        root.download_options = {'defaultextension': selected_format, 'initialfile': root.filename}

        # Download file
        file_path = os.path.abspath(audio_file)
        root.download_url = "file://" + file_path
        root.download_from_url()

# Add label for instructions
instructions_label = tk.Label(root, text="Select a video file to convert to audio:")
instructions_label.pack()

# Add button to open file dialog
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

# Add label for selecting audio format
format_label = tk.Label(root, text="Select an audio format:")
format_label.pack()

# Add dropdown for selecting audio format
format_var = tk.StringVar(root)
format_var.set(AUDIO_FORMATS[0])
format_dropdown = tk.OptionMenu(root, format_var, *AUDIO_FORMATS)
format_dropdown.pack()

# Add button to convert file
convert_button = tk.Button(root, text="Convert", command=convert_file)
convert_button.pack()

# Add button to download file
download_button = tk.Button(root, text="Download", command=download_file)
download_button.pack()

# Add label for displaying messages
message_label = tk.Label(root, text="")
message_label.pack()

# Run the GUI window
root.mainloop()
