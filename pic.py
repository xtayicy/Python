import pytesseract as pt
from PIL import Image

path = r"E:\Tesseract-OCR\tesseract.exe";

pt.pytesseract.tesseract_cmd = path;

img = Image.open("01.jpg");

text = pt.image_to_string(img);

print(text)