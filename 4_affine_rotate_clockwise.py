import cv2
import numpy as np


srcImg = cv2.imread('xs.jpg')  # 前景图像
bgImg = cv2.imread('earth_light.jpg')  # 背景图像
cv2.namedWindow('dstImg', 0)

while True:
    for i in range(0, 361):
        theta = i*np.pi/180  # 定义角度
        # 定义仿射矩阵
        turnArray = np.array([
            [np.cos(theta), -np.sin(theta), 500],
            [np.sin(theta), np.cos(theta), 500]
        ], dtype=np.float32)
        # 调用仿射变换函数
        turnImage = cv2.warpAffine(srcImg, turnArray, (1080, 1080))
        # 图像融合
        dst = cv2.addWeighted(turnImage, 0.8, bgImg, 0.2, 0)
        cv2.imshow('dstImg', dst)
        cv2.waitKey(25)

cv2.destroyAllWindows()