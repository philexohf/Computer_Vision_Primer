# ===============程序功能：霍夫直线检测============== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np

img = cv2.imread('./image/houghlines.png')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edgeImg = cv2.Canny(grayImg, 50, 150)
minLineLength = 20
maxLineGap = 5
color = (0, 0, 255)
houghLine = cv2.HoughLinesP(edgeImg, 1, np.pi/180, 100, minLineLength, maxLineGap)

for x1, y1, x2, y2 in houghLine[0]:
    cv2.line(img, (x1, y1), (x2, y2), color, 2)

cv2.namedWindow('edges', 0)
cv2.namedWindow('HoughLines', 0)
cv2.imshow('edges', edgeImg)
cv2.imshow('HoughLines', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
