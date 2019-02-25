import cv2
import numpy as np
import random

srcImg = cv2.imread('summer.png')
cv2.namedWindow('srcImg')
cv2.namedWindow('test', 0)
cv2.imshow('srcImg', srcImg)
while True:
    i = random.randint(0, 360)
    theta = i * np.pi / 180
    rotMatrix = np.array([
        [np.cos(theta), -np.sin(theta), 1000 - 10*random.randint(1, 50)],
        [np.sin(theta), np.cos(theta), 1000 - 10*random.randint(1, 50)]
    ], dtype=np.float32)

    rotImg = cv2.warpAffine(srcImg, rotMatrix, (2000, 2000))
    cv2.imshow('test', rotImg)
    cv2.waitKey(666)

cv2.destroyAllWindows()