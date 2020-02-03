# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np

srcImg = cv2.imread('./image/tamamonomae0.png')  # 前景图像
bgImg = cv2.imread('./image/earth_light.jpg')  # 背景图像
cv2.namedWindow('Edge', 0)
cv2.namedWindow('InvEdge', 0)
cv2.namedWindow('SrcRotImg', 0)
cv2.namedWindow('DstRotImg', 0)

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
        srcRotImg = cv2.addWeighted(rotImg, 0.8, bgImg, 0.2, 0)
        blurImg = cv2.medianBlur(rotImg, 7)  # blurKsize = 7
        grayImg = cv2.cvtColor(blurImg, cv2.COLOR_BGR2GRAY)
        cv2.Laplacian(grayImg, cv2.CV_8U, grayImg, 5)  # edgeKsize = 5

        invGrayImg = (1.0 / 255) * (255 - grayImg)
        global lapRotImg
        channels = cv2.split(rotImg)
        for channel in channels:
            channel[:] = channel * invGrayImg
            lapRotImg = cv2.merge(channels, grayImg)
        # 图像融合
        dstRotImg = cv2.addWeighted(lapRotImg, 0.8, bgImg, 0.2, 0)

        cv2.imshow('Edge', grayImg)
        cv2.imshow('InvEdge', invGrayImg)
        cv2.imshow('SrcRotImg', srcRotImg)
        cv2.imshow('DstRotImg', dstRotImg)
        cv2.waitKey(30)
