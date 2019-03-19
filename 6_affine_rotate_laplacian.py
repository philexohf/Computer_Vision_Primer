import cv2
import numpy as np


srcImg = cv2.imread('./image/summer.png')  # 前景图像
bgImg = cv2.imread('./image/earth_light.jpg')  # 背景图像
cv2.namedWindow('test')

while True:
    for i in range(360):
        theta = i * np.pi / 180  # 定义角度
        # 定义仿射矩阵
        rotArr = np.array([
            [np.cos(theta), -np.sin(theta), 500],
            [np.sin(theta), np.cos(theta), 500]
        ], dtype=np.float32)
        # 调用仿射变换函数
        rotImg = cv2.warpAffine(srcImg, rotArr, (1080, 1080))
        blurImg = cv2.medianBlur(rotImg, 7)  # blurKsize = 7
        grayImg = cv2.cvtColor(blurImg, cv2.COLOR_BGR2GRAY)
        cv2.Laplacian(grayImg, cv2.CV_8U, grayImg, 5)  # edgeKsize = 5
        cv2.imshow('laplaceEdge', grayImg)
        NIA = (1.0 / 255) * (255 - grayImg)
        cv2.imshow('NIA-laplaceEdge', NIA)
        channels = cv2.split(rotImg)
        for channel in channels:
            channel[:] = channel * NIA
            rotImg = cv2.merge(channels, grayImg)
        # 图像融合
        addImg = cv2.addWeighted(rotImg, 0.8, bgImg, 0.2, 0)
        cv2.imshow('test', addImg)
        cv2.waitKey(30)

cv2.destroyAllWindows()
