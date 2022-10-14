
from captcha.image import ImageCaptcha
import string
import random

N = 7
res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
str1 = str(res)
image = ImageCaptcha(width = 300, height = 100)
captcha_text = str1
data = image.generate(captcha_text)
image.write(captcha_text, 'C:\\Users\\admin\\Documents\\Python\\Projects\\RCG\\CAPTCHA.png')
from PIL import Image
Image.open('C:\\Users\\admin\\Documents\\Python\\Projects\\RCG\\CAPTCHA.png')
