from PIL import Image
import pytesseract
from pytesseract import image_to_string
import textract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#im=Image.open(r'test.png')
#print(image_to_string(im))
text = textract.process("test.png")
print(text)