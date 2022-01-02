from skimage import io
from scipy.spatial.distance import cosine
import numpy as np
import os


def balanceRGB(image):

    return image

    # balancedImage = np.zeros(image.shape[:2])

    # for row in range(len(image)):
    #     for col in range(len(image[0])):
    #         if(len(image[row, col]) != 3):
    #             raise Exception("not a standard rgb")
    #         balancedImage[row, col] = (int(image[row, col, 0])
    #             + int(image[row, col, 1]) + int(image[row, col, 2])) / 3

    # return balancedImage
            


afterImage = io.imread("referencePics/after.png")
maxCosNum = -1
maxGeneratedFile = ""

for file in os.scandir("generatedPics"):
    if(file.is_file() and file.name.endswith("png")):
        generatedImage = io.imread(file.path)

        afterVec = balanceRGB(afterImage).flatten()
        generatedVec = balanceRGB(generatedImage).flatten()
        cosNum = 1 - cosine(afterVec, generatedVec)

        if(cosNum > maxCosNum):
            maxCosNum = cosNum
            maxGeneratedFile = file.name

print(maxCosNum)
print(maxGeneratedFile)



