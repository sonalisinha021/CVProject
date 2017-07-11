import skimage.io as io
import skimage.color as color
from skimage import filters
import matplotlib as plt
from skimage.color import rgb2gray 
import cv2

from PIL import Image
import pytesseract
from pytesseract import image_to_string
#import textract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

basewidth = 4000
img=Image.open('so-0.jpg')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save('resized_image.jpg')
#print(image_to_string(im))

#img = io.imread('resized_image.jpg')
#img_grayscale = rgb2gray(img)
#io.imsave('resized_image1.jpg',img_grayscale)

im_gray = cv2.imread('resized_image.jpg', cv2.IMREAD_GRAYSCALE)
thresh = 100
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('thresh.jpg', im_bw)

img2=Image.open('thresh.jpg')
print(image_to_string(img2).encode('utf-8'))
#text = textract.process("test.png")
#print(text)



                    
    
    
    
    
    
    
    
    
    
#https://stackoverflow.com/questions/7624765/converting-an-opencv-image-to-black-and-white    