import PIL
from PIL import Image
import pytesseract



def read_text(filename):
    img1 = PIL.Image.open(filename)
    text = pytesseract.image_to_string(img1)
    text = text.upper()
    return text


def grab_number(string, word):
    index = string.find(word)
    number = ""
    while not (string[index].isdigit()):
        index += 1
    while (index < len(string)) and (string[index].isdigit()):
        number += string[index]
        index += 1
    return int(number)

#text = read_text('IMG1.jpg')
#print(text)
#print(grab_number(text, "CALORIES"))






