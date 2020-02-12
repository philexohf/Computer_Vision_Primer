# ====程序功能：用Canny算子处理灰度图像得到物体边缘===== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2

img = cv2.imread("./image/tamamonomae1.png")
cv2.namedWindow('img')
cv2.namedWindow('canny')

blurImg = cv2.GaussianBlur(img, (3, 3), 0)
grayImg = cv2.cvtColor(blurImg, cv2.COLOR_BGR2GRAY)
cannyImg = cv2.Canny(grayImg, 50, 150)
cv2.imshow('img', img)
cv2.imshow("canny", cannyImg)
cv2.imwrite("canny.jpg", cannyImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
