# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./image/flower.png')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret1, thresh = cv2.threshold(grayImage, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
openOpt = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
bgImg = cv2.dilate(openOpt, kernel, iterations=3)
distTrans = cv2.distanceTransform(openOpt, cv2.DIST_L2, 5)
ret2, fgImg = cv2.threshold(distTrans, 0.7 * distTrans.max(), 255, 0)
fgImg = np.uint8(fgImg)
x = cv2.subtract(bgImg, fgImg)
ret, markers = cv2.connectedComponents(fgImg)
markers += 1
markers[255 == x] = 0

markers = cv2.watershed(image, markers)
image[-1 == markers] = [255, 0, 0]
plt.xticks([])
plt.yticks([])
plt.imshow(image)
plt.show()
