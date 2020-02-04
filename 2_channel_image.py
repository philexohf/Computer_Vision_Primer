# ===程序功能：BGR颜色通道的操作=== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np

img = cv2.imread("./image/summer.png")
dstImg = img.copy()  # 获取img图像数据的copy

# dstImg[:, :, 2] = 0  # 红色通道置零
dstImg[:, :, 1] = 0  # 绿色通道置零
# dstImg[:, :, 0] = 0  # 蓝色通道置零
# dstImg[250:600, 200:400, 1] = 0  # 区域(高：250-600，宽：200-400)绿色通道置零
dst = np.hstack([img, dstImg])  # 将img和dstImg两幅图片合并在一起

cv2.namedWindow('BGR-channel', 0)
cv2.imshow('BGR-channel', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
