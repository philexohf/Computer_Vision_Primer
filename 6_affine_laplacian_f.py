import cv2
import numpy as np


def laplacian_operate(affineImage):
    blurImage = cv2.medianBlur(affineImage, 7)  # blurKsize = 7
    grayImage = cv2.cvtColor(blurImage, cv2.COLOR_BGR2GRAY)
    cv2.Laplacian(grayImage, cv2.CV_8U, grayImage, 5)  # edgeKsize = 5
    NIA = (1.0 / 255) * (255 - grayImage)
    channels = cv2.split(affineImage)
    for channel in channels:
        channel[:] = channel * NIA
    cv2.merge(channels, affineImage)

srcImg = cv2.imread('./image/xs.jpg')  # 前景图像
bgImg = cv2.imread('./image/earth_light.jpg')  # 背景图像
# cv2.imshow('hnj', srcImg)
cv2.namedWindow('dst', 0)
# 循环处理图片帧
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
        laplacian_operate(affineImage)  # 调用拉普拉斯算子进行边缘处理的函数
        # 图像融合
        addImage = cv2.addWeighted(affineImage, 0.8, bgImg, 0.2, 0)
        cv2.imshow('dst', addImage)
        cv2.waitKey(25)

cv2.destroyAllWindows()
