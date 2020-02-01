import cv2
import os

path = "./image"
img = cv2.imread(os.path.join(path, 'lancelot_guinevere.jpg'))  # os.path.join()路径拼接
cv2.namedWindow('src')
cv2.imshow('src', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.Laplacian(gray, cv2.CV_8U, gray, 5)
gray = cv2.GaussianBlur(gray, (9, 9), 0)
dst = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
cv2.namedWindow('laplacian')
cv2.imshow('laplacian', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
