import cv2

img = cv2.imread("test.jpg")
cv2.namedWindow('img', 0)
cv2.namedWindow('cannyImage', 0)
cv2.namedWindow('dstImage', 0)
cv2.imshow('img', img)
blurImage = cv2.GaussianBlur(img, (3, 3), 0)
grayImage = cv2.cvtColor(blurImage, cv2.COLOR_BGR2GRAY)
cannyImage = cv2.Canny(grayImage, 30, 150)
cv2.imshow("cannyImage", cannyImage)
cv2.imwrite("cannyImage.jpg", cannyImage)
dst = cv2.bitwise_and(img, img, mask=cannyImage)
cv2.imshow('dstImage', dst)
cv2.imwrite("dstImage.jpg", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


