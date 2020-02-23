# ===程序功能：边界框、最小矩形区域和最小闭合圆形轮廓的绘制=== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np

img = 255 - cv2.imread('./image/github.png', cv2.IMREAD_UNCHANGED)  # 图片反色
cv2.imshow('src', img)
img = cv2.pyrDown(img)  # 构建图像金字塔，图像尺寸变小，分辨率降低
ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY),
                            127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    # 边界区域坐标
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    rect = cv2.minAreaRect(c)  # 找到最小区域
    box = cv2.boxPoints(rect)  # 计算最小区域坐标
    box = np.int0(box)
    # 绘制轮廓
    cv2.drawContours(img, [box], 0, (0, 0, 255), 3)
    # 计算最小包围圆形的中心和半径
    (x, y), radius = cv2.minEnclosingCircle(c)
    center = (int(x), int(y))
    radius = int(radius)
    # 绘制圆形
    img = cv2.circle(img, center, radius, (0, 255, 0), 2)

cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.namedWindow('contours', 0)
cv2.imshow('contours', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
