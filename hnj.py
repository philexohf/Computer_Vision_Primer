import cv2
import numpy as np
import random

img = cv2.imread('xs.png')
imgx = cv2.imread('ev.jpg')
cv2.imshow('yste', img)

while True:
    i = 0
    while i <= 360:
        theta = i * np.pi / 180
        matrixAffine = np.array([
            [np.cos(theta), -np.sin(theta), 500 - 10 * random.randint(1, 10)],
            [np.sin(theta), np.cos(theta), 500 - 10 * random.randint(1, 10)]
        ], dtype=np.float32)

        imgAffine = cv2.warpAffine(img, matrixAffine, (1080, 1080))
        dst = cv2.addWeighted(imgAffine, 0.7, imgx, 0.3, 0)
        cv2.imshow('yste', dst)
        i += 1
        cv2.waitKey(30)

cv2.destroyAllWindows()