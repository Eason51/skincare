import cv2
from SkinDetector import skin_detector

def detect_skin(img, threshold=0.5):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    mask = skin_detector.process(img, thresh=threshold)
    return mask


