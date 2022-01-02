from numpy import imag
import numpy
from skimage import io
from skimage.draw import line, rectangle
from skimage.restoration import denoise_bilateral
from bilateral_filter import filter_bilateral
from bilateral_filter2 import bilateralfilter
from skimage.color import rgb2gray, rgba2rgb

image = io.imread("face.jpg")
# image = denoise_bilateral(image, sigma_color=0.05, sigma_spatial=10, multichannel=True, bins=10)
# image = filter_bilateral(image, 10, 100)
greyImage = rgb2gray(image)

image = bilateralfilter(image, greyImage, 1, 0.1*255)

io.imsave("face2.jpg", image)
