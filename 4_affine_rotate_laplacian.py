import cv2
import numpy as np


srcImg = cv2.imread('xs.jpg')  # 前景图像
bgImg = cv2.imread('earth_light.jpg')  # 背景图像
cv2.namedWindow('test', 0)

while True:
    for i in range(0, 361):
        theta = i * np.pi / 180  # 定义角度
        # 定义仿射矩阵
        affArray = np.array([
            [np.cos(theta), -np.sin(theta), 500],
            [np.sin(theta), np.cos(theta), 500]
        ], dtype=np.float32)
        # 调用仿射变换函数
        affineImage = cv2.warpAffine(srcImg, affArray, (1080, 1080))
        blurImage = cv2.medianBlur(affineImage, 7)  # blurKsize = 7
        grayImage = cv2.cvtColor(blurImage, cv2.COLOR_BGR2GRAY)
        cv2.Laplacian(grayImage, cv2.CV_8U, grayImage, 5)  # edgeKsize = 5
#        cv2.imshow('lap', grayImage)
        NIA = (1.0 / 255) * (255 - grayImage)
#        cv2.imshow('NIA', NIA)
        channels = cv2.split(affineImage)
        for channel in channels:
            channel[:] = channel * NIA
        affineImage = cv2.merge(channels, grayImage)
        # 图像融合
        addImg = cv2.addWeighted(affineImage, 0.8, bgImg, 0.2, 0)
        cv2.imshow('test', addImg)
        cv2.waitKey(25)

cv2.destroyAllWindows()
