import cv2
import numpy as np

img = cv2.imread('./image/houghcircles.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayImg = cv2.medianBlur(grayImg, 5)

houghCircle = cv2.HoughCircles(grayImg, cv2.HOUGH_GRADIENT, 1, 120,
                               param1=100, param2=30, minRadius=0, maxRadius=0)
houghCircle = np.uint16(np.around(houghCircle))

for i in houghCircle[0, :]:
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)  # 画外圆
    cv2.circle(img, (i[0], i[1]), 2, (0, 255, 0), 3)  # 画圆心

cv2.namedWindow('HoughCirles', 0)
cv2.imshow('HoughCirles', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
