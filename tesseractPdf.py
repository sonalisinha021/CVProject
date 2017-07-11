from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io


tool = pyocr.get_available_tools()[0] #tesseract
lang = tool.get_available_languages()[1] #english

req_image = []
final_text = []

image_pdf = Image(filename="POC.pdf", resolution=300)

image_jpeg = image_pdf.convert('jpeg')

#page=image_pdf.sequence[0] #won't be able to save single image
image_pdf.compression_quality = 100 #
image_pdf.save(filename="so" + ".jpg")

for img in image_jpeg.sequence:
  #  img.save(filename='pikachu.jpg')
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))
   
for img in req_image:    
    txt = tool.image_to_string(
        PI.open(io.BytesIO(img)),
        lang="eng",
        builder=pyocr.builders.TextBuilder()
    ).encode('utf-8')
   # print(txt)
    final_text.append(txt)
    print(final_text)