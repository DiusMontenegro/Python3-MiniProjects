import tkinter as tk
from tkinter import filedialog
import zipfile
import threading

class App:
    def __init__(self, master):
        self.master = master
        master.title("File Compressor")
        
        # Create GUI elements
        self.select_file_button = tk.Button(master, text="Select File", command=self.select_file)
        self.select_file_button.pack()

        self.filename_label = tk.Label(master, text="No file selected")
        self.filename_label.pack()

        self.output_path_button = tk.Button(master, text="Select Output Path", command=self.select_output_path)
        self.output_path_button.pack()

        self.output_path_label = tk.Label(master, text="No output path selected")
        self.output_path_label.pack()

        self.compress_button = tk.Button(master, text="Compress", command=self.compress_file)
        self.compress_button.pack()

        self.progress_label = tk.Label(master, text="")
        self.progress_label.pack()

    def select_file(self):
        self.filename = filedialog.askopenfilename()
        self.filename_label.config(text=self.filename)

    def select_output_path(self):
        self.output_path = filedialog.askdirectory()
        self.output_path_label.config(text=self.output_path)

    def compress_file(self):
        try:
            # Start a separate thread to compress the file
            t = threading.Thread(target=self.compress_file_thread)
            t.start()
        except:
            self.progress_label.config(text="Error: Could not start compression thread")

    def compress_file_thread(self):
        try:
            # Open the selected file
            with zipfile.ZipFile(self.output_path + "/compressed.zip", "w", compression=zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(self.filename)
            
            self.progress_label.config(text="Compression complete")
        except:
            self.progress_label.config(text="Error: Could not compress file")

# Create the GUI
root = tk.Tk()
app = App(root)
root.mainloop()
