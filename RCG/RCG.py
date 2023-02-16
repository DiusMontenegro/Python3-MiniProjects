import phonenumbers     # import phonenumbers library
from phonenumbers import PhoneNumber, geocoder    # import necessary functions from phonenumbers library
from langdetect import detect   # import detect function from langdetect library
from captcha.image import ImageCaptcha  # import ImageCaptcha for generating captcha image
import string   # import string library for generating random text
import random   # import random library for generating random text

# Generate a random string for the captcha image
N = 7
captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

# Generate the captcha image and save it to a file
image = ImageCaptcha(width=300, height=100)
data = image.generate(captcha_text)
image.write(captcha_text, 'CAPTCHA.png')

# Display the captcha image to the user
from PIL import Image
Image.open('CAPTCHA.png').show()

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
else:
    # If the captcha is incorrect, print an error message
    print("Incorrect CAPTCHA code. Please try again.")
