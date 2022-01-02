from face_recognition.api import face_landmarks
from numpy.lib.polynomial import _raise_power
from skimage import io
from skimage.draw import line, rectangle
from numpy import array

import face_recognition
from skimage.draw import polygon2mask
from skimage.draw.draw import polygon
from skimage.util.dtype import img_as_float
image = face_recognition.load_image_file("face.jpg")
face_locations = face_recognition.face_locations(image)
import cv2

from bilateral_filter2 import apply_bilateralFilter
# if(len(face_locations) != 0):
#     face_location = face_locations[0]
# else:
#     raise Exception("no face found")
# (top, right, bottom, left) = (face_location[0], face_location[1], face_location[2], face_location[3])
    

# image = io.imread("face.jpg")
# print(face_location)
# print(image.shape)
# row, column = rectangle((top, left), (bottom, right))
# image[row, column] = [255, 0, 255]
# io.imsave("face2.jpg", image)

face_landmarks_lists = face_recognition.face_landmarks(image)
if(len(face_landmarks_lists) != 0):
    face_landmarks_list = face_landmarks_lists[0]
else:
    raise Exception("no face found")

image = io.imread("face.jpg")

# chin
# left_eyebrow
# right_eyebrow
# nose_bridge
# nose_tip
# left_eye
# right_eye
# top_lip
# bottom_lip

# for pos in face_landmarks_list:
#     chin_list = face_landmarks_list[pos]
#     (prevCol, prevRow) = (-1, -1)
#     for (column, row) in chin_list:
#         if(prevCol == -1):
#             prevCol = column
#             prevRow = row
#             continue
        
#         lineRow, lineCol = line(prevRow, prevCol, row, column)
#         image[lineRow, lineCol] = [255, 0, 255]

#         prevCol = column
#         prevRow = row

# io.imsave("landmark.jpg", image)

def generateMask(image, face_landmarks_list, posName):

    rowArr = []
    columnArr = []
    if(posName in face_landmarks_list):
        pos_list = face_landmarks_list[posName]
        for (column, row) in pos_list:         
            rowArr.append(row)
            columnArr.append(column)

    polygonArr = list(zip(rowArr, columnArr))
    mask = polygon2mask(image.shape, polygonArr) # image[mask] = 255
    return mask


def generateNoseMask(image, face_landmarks_list):
    rowArr = []
    columnArr = []

    rowArr = []
    columnArr = []
    if("nose_tip" in face_landmarks_list):
        pos_list = face_landmarks_list["nose_tip"]
        for (column, row) in pos_list:         
            rowArr.append(row)
            columnArr.append(column)

    if("nose_bridge" in face_landmarks_list):
        pos_list = face_landmarks_list["nose_bridge"]
        (topCol, topRow) = (-1, -1)
        for(column, row) in pos_list:
            if(topRow == -1):
                topCol = column
                topRow = row
                continue

            if(row < topRow):
                topRow = row
                topCol = column
        
        rowArr.append(topRow)
        columnArr.append(topCol)

        polygonArr = list(zip(rowArr, columnArr))
        mask = polygon2mask(image.shape, polygonArr)
        return mask




image_out = image.copy()

sigma_s = 7
sigma_r = 0.1*255
# sigma_s = 7
# sigma_r = 10*255

filteredImg = apply_bilateralFilter(image, sigma_s, sigma_r)

chinMask = generateMask(image, face_landmarks_list, "chin")
topLipMask = generateMask(image, face_landmarks_list, "top_lip")
bottomLipMask = generateMask(image, face_landmarks_list, "bottom_lip")
noseMask = generateNoseMask(image, face_landmarks_list)

image_out[chinMask] = filteredImg[chinMask]
image_out[topLipMask] = image[topLipMask]
image_out[bottomLipMask] = image[bottomLipMask]
image_out[noseMask] = image[noseMask]

print(image[250, 250])
print(chinMask[250, 250])


io.imsave("face2.jpg", image_out)
# io.imsave("face2.jpg", chinMask)


