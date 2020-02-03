# https://github.com/philexohf/Computer_Vision_Primer
import cv2

bgImg = cv2.imread('./image/test.jpg')
logoImg = cv2.imread('./image/github.png')

rows, cols, channels = logoImg.shape
roi = bgImg[0:rows, 0:cols]
# 创建mask of logo和inverse mask
img2gray = cv2.cvtColor(logoImg, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# 取 roi 中与 mask 中不为零的值对应的像素的值，其他值为 0
# 注意这里必须有 mask=mask 或者 mask=mask_inv, 其中的 mask= 不能忽略
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
# 取 roi 中与 mask_inv 中不为零的值对应的像素的值，其他值为 0。

img2_fg = cv2.bitwise_and(logoImg, logoImg, mask=mask_inv)

dst = cv2.add(img1_bg, img2_fg)
bgImg[0:rows, 0: cols] = dst
cv2.imshow('res', bgImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
