import cv2
import numpy as np

img = cv2.imread('xs.jpg')
cv2.imshow('srcImg', img)
# 沿着横纵轴放大1.6倍，然后平移(-150,-240)，最后沿原图大小截取，等效于裁剪并放大
M_crop_xs = np.array([
    [5, 0, -1000],
    [0, 5, -600]
], dtype=np.float32)

img_xs = cv2.warpAffine(img, M_crop_xs, (1000, 1000)) #仿射变换函数
cv2.imshow('xs1', img_xs)

# x轴的剪切变换，角度15°
theta = 45 * np.pi / 180
M_shear = np.array([
    [1, np.tan(theta), 0],
    [0, 1, 0]
], dtype=np.float32)

img_sheared = cv2.warpAffine(img, M_shear, (1000, 1000))
cv2.imshow('xs2', img_sheared)

# 顺时针旋转，角度15°
M_rotate = np.array([
    [np.cos(theta), -np.sin(theta), 500],
    [np.sin(theta), np.cos(theta), 0]
], dtype=np.float32)

img_rotated = cv2.warpAffine(img, M_rotate, (1000, 1000))
cv2.imshow('xs3', img_rotated)

# 某种变换，具体旋转+缩放+旋转组合可以通过SVD分解理解
M = np.array([
    [1, 1.5, -400],
    [0.5, 2, -100]
], dtype=np.float32)

img_transformed = cv2.warpAffine(img, M, (1000, 1000))
cv2.imshow('xs4.jpg', img_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
