import cv2


img = cv2.imread('earthlight.jpg')
# path = "C:/Users/Administrator/Pictures/"
# img = cv2.imread(path + 'earthlight.jpg')
cv2.namedWindow('img', 0)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
