import cv2


img = cv2.imread('./image/summer.png')  # 读取当前目录下的图片.
cv2.namedWindow('img', 0)  # 创建一个窗口，参数0表示窗口大小可改变.
cv2.imshow('img', img)  # 显示图片，第一个参数是显示图像的窗口的名字，第二个参数是要显示的图像.

cv2.waitKey(0)
cv2.destroyAllWindows()
