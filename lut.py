import cv2
from skimage import io 
from detectSkin import detect_skin
import numpy as np
from magic_face.magic_face.makeup import whitening
from scipy.spatial.distance import cosine

beforeImage = io.imread("referencePics/before.png")
mask = detect_skin(beforeImage, threshold=0.1)
fullChannelMask = beforeImage.copy()
for row in range(len(beforeImage)):
    for col in range(len(beforeImage[0])):
        if(mask[row, col] != 0):
            fullChannelMask[row, col] = np.ones(beforeImage.shape[-1])
        else:
            fullChannelMask[row, col] = np.zeros(beforeImage.shape[-1])

for strength in np.arange(1.0, 101.0, 0.5):

   inputImage = cv2.cvtColor(beforeImage, cv2.COLOR_RGB2BGR)
   outputImage = whitening(inputImage, fullChannelMask, strength)
   generatedImage = cv2.cvtColor(outputImage, cv2.COLOR_BGR2RGB)     
   
   io.imsave(f"generatedPics/{strength}.png", generatedImage)
