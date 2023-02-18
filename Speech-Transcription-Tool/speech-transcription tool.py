import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import speech_recognition as sr

# Create a GUI window
root = tk.Tk()
root.title("Audio/Video Transcription Tool")

# Set the window size and make it non-resizable
root.geometry("400x200")
root.resizable(False, False)

# Define function to select audio or video file
def select_file():
    file_path = filedialog.askopenfilename(title="Select file", filetypes=(
        ("Audio Files", "*.wav;*.mp3;*.ogg;*.flac"),
        ("Video Files", "*.mp4;*.mov;*.avi;*.mkv")))
    if file_path:
        input_file_path.set(file_path)

# Define function to select output path
def select_output_path():
    output_path = filedialog.asksaveasfilename(title="Save file as", defaultextension=".txt")
    if output_path:
        output_file_path.set(output_path)

# Define function to transcribe the audio or video file
def transcribe():
    file_path = input_file_path.get()
    output_path = output_file_path.get()
    if not file_path:
        messagebox.showerror("Error", "Please select a file to transcribe.")
        return
    if not output_path:
        messagebox.showerror("Error", "Please select an output file path.")
        return

    try:
        # Initialize a recognizer
        r = sr.Recognizer()

        # Transcribe the audio or video file
        with sr.AudioFile(file_path) as source:
            audio = r.record(source)

        # Use Google Web Speech API to transcribe the audio
        text = r.recognize_google(audio, language="en-US", show_all=True)

        # Write the transcribed text to a file with proper punctuation and handling of [inaudible] tags
        with open(output_path, 'w', encoding='utf-8') as f:
            for result in text.get("alternative", []):
                if "transcript" in result:
                    trans = result["transcript"]
                    if not trans.strip():
                        continue
                    if result.get("confidence", 0) < 0.5:
                        trans = f"[inaudible] ({result['confidence']:.2f})"

                    # Replace foreign language with [foreign]
                    if not all(ord(char) < 128 for char in trans):
                        trans = "[foreign]"

                    # Add proper punctuation
                    if not trans.endswith((".", "!", "?", "[inaudible]")):
                        trans += "."

                    f.write(trans + "\n")

        messagebox.showinfo("Transcription successful", "Transcription completed and saved to file.")
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Could not request results from Google Speech Recognition service: {e}")

# Define StringVars for the input file path and output file path
input_file_path = tk.StringVar()
output_file_path = tk.StringVar()

# Create input file label and button
input_label = ttk.Label(root, text="Select file to transcribe:")
input_label.pack(pady=5)
input_frame = ttk.Frame(root)
input_frame.pack()
input_entry = ttk.Entry(input_frame, textvariable=input_file_path, state="readonly", width=40)
input_entry.pack(side="left")
input_button = ttk.Button(input_frame,
text="Browse",
                         command=select_file)
input_button.pack(side="left")

# Create output file label and button
output_label = ttk.Label(root, text="Select output file path:")
output_label.pack(pady=5)
output_frame = ttk.Frame(root)
output_frame.pack()
output_entry = ttk.Entry(output_frame, textvariable=output_file_path, state="readonly", width=40)
output_entry.pack(side="left")
output_button = ttk.Button(output_frame,

                          text="Browse", 
                          command=select_output_path) 
output_button.pack(side="left") 
 
# Create a transcribe button 
transcribe_button = ttk.Button(root, 

                              text="Transcribe", 
                              command=transcribe) 
transcribe_button.pack() 

 # Run the GUI window infinitely until it is closed  
root.mainloop()
