from skimage.transform import resize
from skimage import io

beforeImage = io.imread("referencePics/before.jpg")
afterImage = io.imread("referencePics/after.jpg")

if(beforeImage.shape[0] != afterImage.shape[0] or 
    beforeImage.shape[1] != afterImage.shape[1]):

    beforeArea = beforeImage.shape[0] * beforeImage.shape[1]
    afterArea = afterImage.shape[0] * afterImage.shape[1]

    if(beforeArea >= afterArea):
        beforeImage = resize(beforeImage, afterImage.shape)
    else:
        afterImage = resize(afterImage, beforeImage.shape)

io.imsave("referencePics/before.png", beforeImage)
io.imsave("referencePics/after.png", afterImage)
