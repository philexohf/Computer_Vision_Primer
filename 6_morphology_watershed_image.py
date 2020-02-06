import cv2
import numpy as np

img = cv2.imread('./image/rose.jpg')
blur = cv2.GaussianBlur(img, (5, 5), 0)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
# 二值化处理
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# 开操作
kennel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mb = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kennel, iterations=2)
# 膨胀
sure_bg = cv2.dilate(mb, kennel, iterations=3)
# 进行距离变换
dist = cv2.distanceTransform(mb, cv2.DIST_L2, 3)
dist_output = cv2.normalize(dist, 0, 1.0, cv2.NORM_MINMAX) * 50

ret, surface = cv2.threshold(dist, 0, 1.0, cv2.NORM_MINMAX)  # 优化图像
surface_fg = np.uint8(surface)  # 转为种子
x = cv2.subtract(sure_bg, surface_fg)  # 除种子外的部分
ret, markers = cv2.connectedComponents(surface_fg)  # 连接部分
print(ret)

markers += 1
markers[x == 255] = 0  # 像素操作
# 分水岭
markers = cv2.watershed(img, markers=markers)
img[markers == -1] = [0, 0, 255]  # 在原图上绘制分水线

cv2.namedWindow('binary', 0)
cv2.namedWindow('sure_bg', 0)
cv2.namedWindow('dist_output', 0)
cv2.namedWindow('surface', 0)
cv2.namedWindow('img', 0)

cv2.imshow('binary', binary)
cv2.imshow('sure_bg', sure_bg)
cv2.imshow('dist_output', dist_output)  # 图中最亮的区域是种子
cv2.imshow('surface', surface)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
