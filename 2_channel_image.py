# ===程序功能：BGR颜色通道的操作=== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2

img = cv2.imread("./image/summer.png")
cv2.imshow('src', img)
# img[:, :, 2] = 0  # 红色通道置零
img[250:600, 200:400, 1] = 0  # 区域(高：250-600，宽：200-400)绿色通道置零
# img[:, :, 0] = 0  # 蓝色通道置零
cv2.imshow('dst', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
