# https://github.com/philexohf/Computer_Vision_Primer
import cv2

img = cv2.imread("./image/tamamonomae1.png")
cv2.namedWindow('srcImg')
cv2.namedWindow('cannyImage')

blurImage = cv2.GaussianBlur(img, (3, 3), 0)
grayImage = cv2.cvtColor(blurImage, cv2.COLOR_BGR2GRAY)
cannyImage = cv2.Canny(grayImage, 50, 150)
cv2.imshow('srcImg', img)
cv2.imshow("cannyImage", cannyImage)
# cv2.imwrite("cannyImage.jpg", cannyImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
