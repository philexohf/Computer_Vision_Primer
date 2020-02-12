# ===程序功能：可以用滑条调节Canny()函数阈值的边缘检测=== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2
'''
Canny()函数的2个阈值参数说明：
    低于阈值1的像素点会被认为不是边缘；
    高于阈值2的像素点会被认为是边缘；
    在阈值1和阈值2之间的像素点,若与第2步得到的边缘像素点相邻，则被认为是边缘，否则被认为不是边缘。
'''


def nothing(x):
    pass


img = cv2.imread("./image/tamamonomae1.png")
cv2.namedWindow('img')
cv2.namedWindow('canny')
cv2.imshow('img', img)

# 创建改变阈值的滑条
cv2.createTrackbar('thre1', 'canny', 0, 255, nothing)  # 参数：滑条名，窗口名，数值范围
cv2.createTrackbar('thre2', 'canny', 0, 255, nothing)

blurImg = cv2.GaussianBlur(img, (3, 3), 0)
grayImg = cv2.cvtColor(blurImg, cv2.COLOR_BGR2GRAY)


while True:    
    thre1 = cv2.getTrackbarPos('thre1', 'canny')  # 获取阈值1滑条位置
    thre2 = cv2.getTrackbarPos('thre2', 'canny')  # 获取阈值2滑条位置
    cannyImg = cv2.Canny(grayImg, threshold1=thre1, threshold2=thre2)
    
    cv2.imshow("canny", cannyImg)

    qKey = cv2.waitKey(30) & 0xFF
    if qKey == 27:
        break

cv2.destroyAllWindows()
