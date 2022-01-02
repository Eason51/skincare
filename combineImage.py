def combine_Image(img1, img2, mask):

    outputImg = img1.copy()

    for row in range(len(img1)):
        for col in range(len(img1[0])):
            if(mask[row, col] != 0):
                outputImg[row, col] = img2[row, col]

    return outputImg
