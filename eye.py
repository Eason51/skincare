from face_recognition.api import face_landmarks
from numpy.lib.polynomial import _raise_power
from skimage import io
from skimage.draw import line, rectangle
from numpy import array

import face_recognition
from skimage.draw import polygon2mask
from skimage.draw.draw import polygon
from skimage.util.dtype import img_as_float
import cv2

from bilateral_filter2 import apply_bilateralFilter




image = io.imread("eye.jpg")


sigma_s = 7
sigma_r = 0.1*255

filteredImg = apply_bilateralFilter(image, sigma_s, sigma_r)


io.imsave("eye2.jpg", filteredImg)
# io.imsave("face3.jpg", filteredImg)


