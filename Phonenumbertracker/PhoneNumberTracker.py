import phonenumbers
from phonenumbers import PhoneNumber, geocoder

a = input("Enter the phone number: ")
phonenumber = phonenumbers.parse(a)

print(geocoder.description_for_number(phonenumber, 'en'))
