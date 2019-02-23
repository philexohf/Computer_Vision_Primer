import cv2
import numpy as np
import random

srcImg = cv2.imread('xs.jpg')
bgImg = cv2.imread('earth_light.jpg')
cv2.namedWindow('dst', 0)

while True:
    for i in range(360):
        theta = i * np.pi / 180
        M_rotate = np.array([
            [np.cos(theta), -np.sin(theta), 500 - 10*random.randint(1,10)],
            [np.sin(theta), np.cos(theta), 500 - 10*random.randint(1,10)]
        ], dtype=np.float32)

        img_rotated = cv2.warpAffine(srcImg, M_rotate, (1080, 1080))
        dst = cv2.addWeighted(img_rotated, 0.7, bgImg, 0.3, 0)
        cv2.imshow('dst', dst)
        cv2.waitKey(25)

cv2.destroyAllWindows()