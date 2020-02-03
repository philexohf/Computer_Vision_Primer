# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./image/whj.png')
cv2.namedWindow('srcImg', 0)
cv2.imshow('srcImg', img)

# 沿着横纵轴放大1.6倍，然后平移(-150,-240)，最后沿原图大小截取，等效于裁剪并放大
cropArr = np.array([
    [5, 0, -1000],
    [0, 5, -600]
], dtype=np.float32)
cropImg = cv2.warpAffine(img, cropArr, (1000, 1000))  # 仿射变换函数

# x轴的剪切变换，角度15°
theta = 15 * np.pi / 180
shearArr = np.array([
    [1, np.tan(theta), 0],
    [0, 1, 0]
], dtype=np.float32)
shearImg = cv2.warpAffine(img, shearArr, (1000, 1000))

# 顺时针旋转，角度15°
rotArr = np.array([
    [np.cos(theta), -np.sin(theta), 500],
    [np.sin(theta), np.cos(theta), 0]
], dtype=np.float32)
rotImg = cv2.warpAffine(img, rotArr, (1000, 1000))

# 某种变换，具体旋转+缩放+旋转组合可以通过SVD分解理解
svdArr = np.array([
    [1, 1.5, -400],
    [0.5, 2, -100]
], dtype=np.float32)
svdImg = cv2.warpAffine(img, svdArr, (1000, 1000))

# 将处理后的图像水平合并显示
affineImg = np.hstack([
        cropImg,
        shearImg,
        rotImg,
        svdImg,
    ])

plt.figure(figsize=(20, 16))
plt.xticks(())
plt.yticks(())
plt.imshow(affineImg[:, :, ::-1])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
