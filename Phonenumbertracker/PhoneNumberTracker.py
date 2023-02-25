import phonenumbers
from phonenumbers import PhoneNumber, geocoder
from langdetect import detect
import tkinter as tk
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename()
    return file_path

def get_phone_info():
    input_number = e.get().strip()  # Strip any whitespace characters from the input
    if not input_number:
        # If the input is empty or whitespace-only, display an error message
        output_label.config(text="Error: Please enter a phone number")
        return
    try:
        language = detect(input_number)
    except:
        # If language detection fails, display an error message
        output_label.config(text="Error: Unable to detect language")
        return
    try:
        parsed_number = phonenumbers.parse(input_number)
        country = geocoder.description_for_number(parsed_number, 'en')
        output_label.config(text=f"The phone number is in {language} and is from {country}")
    except:
        # If phone number parsing or geocoding fails, display an error message
        output_label.config(text="Error: Unable to get phone number info")

def process_file():
    file_path = select_file()
    if file_path:
        output_text.delete('1.0', tk.END)
        with open(file_path, 'r') as f:
            for line in f:
                input_number = line.strip()
                try:
                    language = detect(input_number)
                except:
                    output_text.insert(tk.END, f"Error: Unable to detect language for {input_number}\n")
                    continue
                try:
                    parsed_number = phonenumbers.parse(input_number)
                    country = geocoder.description_for_number(parsed_number, 'en')
                    output_text.insert(tk.END, f"The phone number {input_number} is in {language} and is from {country}\n")
                except:
                    output_text.insert(tk.END, f"Error: Unable to get phone number info for {input_number}\n")

root = tk.Tk()
root.title("Phone Number Info")
root.geometry("400x400")

# Create input field
input_label = tk.Label(root, text="Enter phone number:")
input_label.pack()
e = tk.Entry(root)
e.pack()

# Create button to get phone number info
button = tk.Button(root, text="Get phone number info", command=get_phone_info)
button.pack()

# Create label to display output
output_label = tk.Label(root, text="")
output_label.pack()

# Create button to process file
file_button = tk.Button(root, text="Select file to process", command=process_file)
file_button.pack()

# Create text box to display output
output_text = tk.Text(root)
output_text.pack()

root.mainloop()
