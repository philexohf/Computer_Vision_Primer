import cv2
import numpy as np

img = cv2.imread('./image/houghlines.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edgeImg = cv2.Canny(grayImg, 50, 120)
minLineLength = 10
maxLineGap = 5
houghLine = cv2.HoughLinesP(edgeImg, 1, np.pi/180, 100, minLineLength, maxLineGap)

for x1, y1, x2, y2 in houghLine[0]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.namedWindow('edges', 0)
cv2.namedWindow('HoughLines', 0)
cv2.imshow('edges', edgeImg)
cv2.imshow('HoughLines', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
