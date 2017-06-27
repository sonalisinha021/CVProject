import skimage.io as io
import skimage.color as color
from skimage import filters
import matplotlib as plt
from skimage.color import rgb2gray 
img = io.imread('baboon.png')
print(img.shape)
dimensions = color.guess_spatial_dimensions(img)
print(dimensions)

img_grayscale = rgb2gray(img)
print(img_grayscale.shape)


io.imsave('baboon-gs.png',img_grayscale)
show_grayscale = io.imshow(img_grayscale)
plt.show()


edges = filters.sobel(img_grayscale)
io.imshow(edges)
io.show()