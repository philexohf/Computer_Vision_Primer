import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

path = "./image"
img = cv2.imread(os.path.join(path, 'yzq2.png'))  # os.path.join()路径拼接
# 卷积核
kernel_1 = np.array([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]])

kernel_2 = np.array([
    [1, 1, 1],
    [1, -7, 1],
    [1, 1, 1]])

kernel_3 = np.array([
    [-1, -1, -1, -1, -1],
    [-1, 2, 2, 2, -1],
    [-1, 2, 8, 2, -1],
    [-1, 2, 2, 2, -1],
    [-1, -1, -1, -1, -1]]) / 8.0

# # 卷积
# output_1 = cv2.filter2D(img, -1, kernel_1)
# output_2 = cv2.filter2D(img, -1, kernel_2)
# output_3 = cv2.filter2D(img, -1, kernel_3)
#
# cv2.namedWindow('src', 0)
# cv2.namedWindow('kernel_1', 0)
# cv2.namedWindow('kernel_2', 0)
# cv2.namedWindow('kernel_3', 0)
# # 显示锐化效果
# cv2.imshow('src', img)
# cv2.imshow('kernel_1', output_1)
# cv2.imshow('kernel_2', output_2)
# cv2.imshow('kernel_3', output_3)

# 将多个卷积核处理后的图像水平合并起来
output = np.hstack([
        img,
        cv2.filter2D(img, -1, kernel_1),
        cv2.filter2D(img, -1, kernel_1),
        cv2.filter2D(img, -1, kernel_1),
    ])

plt.figure(figsize=(20, 16))
plt.xticks(())
plt.yticks(())
plt.imshow(output[:, :, ::-1])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
