# Phone Number Language and Country of Origin Detection

This Python script prompts the user to enter a phone number and a CAPTCHA code, then uses machine learning to detect the language and country of origin of the phone number. The script generates a random CAPTCHA image to prevent automated spam and fraud attacks.

## Features

- CAPTCHA image generation to prevent automated spam and fraud attacks
- Language detection using the langdetect machine learning library
- Country of origin extraction using the phonenumbers library

## Requirements

- Python 3.x
- `phonenumbers` library (`pip install phonenumbers`)
- `langdetect` library (`pip install langdetect`)
- `captcha` library (`pip install captcha`)
- `Pillow` library (`pip install Pillow`)

## How to use

1. Clone or download the repository to your local machine.
2. Install the required libraries using pip (`pip install -r requirements.txt`).
3. Open a command prompt or terminal window and navigate to the folder where you cloned or downloaded the repository.
4. Run the script using the following command: `python phone_number_detection.py`
5. Follow the prompts to enter a phone number and a CAPTCHA code.

## Example usage

- $ python phone_number_detection.py
- Enter the phone number: +1 650-253-0000
- Enter the CAPTCHA code: XYB2P9K
- The phone number is in en and is from United States

## Acknowledgements

- [phonenumbers library](https://github.com/daviddrysdale/python-phonenumbers)
- [langdetect library](https://github.com/Mimino666/langdetect)
- [captcha library](https://github.com/lepture/captcha)
- [Pillow library](https://github.com/python-pillow/Pillow)
