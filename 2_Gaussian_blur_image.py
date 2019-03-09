import cv2
import os
from matplotlib import pyplot as plt
import numpy as np

path = "./image"
img = cv2.imread(os.path.join(path, 'test.jpg'))  # os.path.join()路径拼接

# 将多个均值平滑处理后的图像水平合并起来
blurImg = np.hstack([
        # img, kernel, std
        cv2.GaussianBlur(img, (3, 3), 0),
        cv2.GaussianBlur(img, (9, 9), 0),
        cv2.GaussianBlur(img, (21, 21), 0),
        cv2.GaussianBlur(img, (49, 49), 0)
    ])

plt.figure(figsize=(10, 8))
plt.imshow(blurImg[:, :, ::-1])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
