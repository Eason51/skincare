from skimage import io 
from detectSkin import detect_skin
from bilateral_filter2 import apply_bilateralFilter
from combineImage import combine_Image
import numpy as np
from magic_face.magic_face.makeup import whitening
import cv2
import os


counter = 0

for file in os.scandir("skinDetectorTest"):
    if(file.is_file() and ("after" in file.name)):
        beforeImage = io.imread(file.path)

        mask = detect_skin(beforeImage, 0.1)
        generatedImage = beforeImage.copy()

        for row in range(len(beforeImage)):
            for col in range(len(beforeImage[0])):
                if(mask[row, col] != 0):
                    generatedImage[row, col] = (255, 0, 255)

        io.imsave(f"skinDetectorTest/after/{counter}.png", beforeImage)
        io.imsave(f"skinDetectorTest/after/{counter}skin.png", generatedImage)

        counter += 1




