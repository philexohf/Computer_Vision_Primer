# =======程序功能：用高斯滤波器对图片进行平滑滤波======= #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

path = "./image"
img = cv2.imread(os.path.join(path, 'test.jpg'))  # os.path.join()路径拼接

# 将多个均值平滑处理后的图像水平合并起来
blurImg = np.hstack([
        cv2.GaussianBlur(img, (3, 3), 0),  # 图像, 高斯核大小, 标准差
        cv2.GaussianBlur(img, (9, 9), 0),
        cv2.GaussianBlur(img, (81, 81), 0),
        cv2.GaussianBlur(img, (201, 201), 0)
    ])

plt.figure(figsize=(20, 16))
plt.xticks([])
plt.yticks([])
plt.imshow(blurImg[:, :, ::-1])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
