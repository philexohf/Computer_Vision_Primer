# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np

srcImg = cv2.imread('./image/whj.png')
cv2.namedWindow('img', 0)

while True:
    for i in range(360):
        theta = i*np.pi/180  # 定义角度
        # 定义仿射矩阵
        rotArr = np.array([
            [np.cos(theta), -np.sin(theta), 1000],
            [np.sin(theta), np.cos(theta), 1000]
        ], dtype=np.float32)
        # 调用仿射变换函数
        rotImg = cv2.warpAffine(srcImg, rotArr, (2000, 2000))
        cv2.imshow('img', rotImg)
        cv2.waitKey(30)
