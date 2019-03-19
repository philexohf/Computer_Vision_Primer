import cv2
import numpy as np


srcImg = cv2.imread('./image/summer.png')  # 前景图像
bgImg = cv2.imread('./image/earth_light.jpg')  # 背景图像
cv2.namedWindow('dst', 1)

while True:
    for i in range(360):
        theta = i*np.pi/180  # 定义角度
        # 定义仿射矩阵
        rotArr = np.array([
            [np.cos(theta), -np.sin(theta), 500],
            [np.sin(theta), np.cos(theta), 500]
        ], dtype=np.float32)
        # 调用仿射变换函数
        rotImg = cv2.warpAffine(srcImg, rotArr, (1080, 1080))
        # 图像融合
        dst = cv2.addWeighted(rotImg, 0.7, bgImg, 0.3, 0)
        cv2.imshow('dst', dst)
        cv2.waitKey(30)

cv2.destroyAllWindows()
