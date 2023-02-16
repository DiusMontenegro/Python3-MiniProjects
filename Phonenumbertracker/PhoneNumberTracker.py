import phonenumbers     # import phonenumbers library
from phonenumbers import PhoneNumber, geocoder    # import necessary functions from phonenumbers library
from langdetect import detect   # import detect function from langdetect library

input_number = input("Enter the phone number: ")    # prompt user to enter phone number
language = detect(input_number)  # detect language of input phone number using langdetect

parsed_number = phonenumbers.parse(input_number)   # parse input phone number using phonenumbers
country = geocoder.description_for_number(parsed_number, 'en')   # extract country of origin of phone number using geocoder

print(f"The phone number is in {language} and is from {country}")   # print the detected language and country of origin of the phone number
