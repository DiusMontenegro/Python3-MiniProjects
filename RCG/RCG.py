import phonenumbers
from phonenumbers import PhoneNumber, geocoder
from langdetect import detect
from captcha.image import ImageCaptcha
import string
import random
from tkinter import filedialog
from tkinter import *

# Initialize the Tkinter GUI
root = Tk()
root.withdraw()

# Prompt the user to select a file to input
input_path = filedialog.askopenfilename(title="Select Input File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

# Prompt the user to select a download path for the output file
download_path = filedialog.askdirectory(title="Select Download Path")

# Generate a random string for the captcha image
N = 7
captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

# Generate the captcha image and save it to a file
image = ImageCaptcha(width=300, height=100)
data = image.generate(captcha_text)
captcha_file = f"{download_path}/CAPTCHA.png"
image.write(captcha_text, captcha_file)

# Display the captcha image to the user
captcha_image = Image.open(captcha_file)
captcha_image.show()

# Prompt the user to enter a phone number and the captcha code
input_number = input("Enter the phone number: ")
captcha_code = input("Enter the CAPTCHA code: ")

# Verify the captcha code
if captcha_code == captcha_text:
    # If the captcha is correct, detect the language of the input phone number
    language = detect(input_number)
    # Parse the phone number and extract the country of origin
    parsed_number = phonenumbers.parse(input_number)
    country = geocoder.description_for_number(parsed_number, 'en')
    # Print the detected language and country of origin of the phone number
    print(f"The phone number is in {language} and is from {country}")
    # Save the output to a file
    output_file = f"{download_path}/output.txt"
    with open(output_file, "w") as f:
        f.write(f"The phone number is in {language} and is from {country}")
else:
    # If the captcha is incorrect, print an error message
    print("Incorrect CAPTCHA code. Please try again.")
