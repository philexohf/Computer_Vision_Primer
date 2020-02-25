# ====程序功能：在图片的ROI区域添加LOGO并保存图片====== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2

img = cv2.imread('./image/test.jpg')
logoImg = cv2.imread('./image/github.png')
cv2.namedWindow('srcImg', 0)
cv2.imshow('srcImg', img)

rows, cols, channels = logoImg.shape  # 获取图像的形状：高度shape[0],宽度shape[1],通道shape[2]
roi = img[0:rows, 0:cols]
# 创建mask of logo和inverse mask
img2gray = cv2.cvtColor(logoImg, cv2.COLOR_BGR2GRAY)  # 彩色图像转灰度图
# 灰度图二值化，小于175的点置0，大于175的点置255
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)  # 按位取反

# 取 roi 中与 mask 中不为零的值对应的像素的值，其他值为 0
# 注意这里必须有 mask=mask 或者 mask=mask_inv, 其中的 mask= 不能忽略
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
# 取 roi 中与 mask_inv 中不为零的值对应的像素的值，其他值为 0。
img2_fg = cv2.bitwise_and(logoImg, logoImg, mask=mask_inv)

add = cv2.add(img1_bg, img2_fg)
img[0:rows, 0: cols] = add
cv2.imwrite('imageWithLOGO.jpg', img)  # 保存处理后的jpg格式图片

cv2.namedWindow('logoImg', 0)
cv2.imshow('logoImg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
