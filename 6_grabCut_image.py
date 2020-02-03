# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np
import matplotlib.pyplot as plt

srcImage = cv2.imread('./image/rose.jpg')
mask1 = np.zeros(srcImage.shape[:2], np.uint8)
bgModel = np.zeros((1, 65), np.float64)
fgModel = np.zeros((1, 65), np.float64)
rect = (50, 50, 600, 479)
cv2.grabCut(srcImage, mask1, rect, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((2 == mask1) | (0 == mask1), 0, 1).astype('uint8')
img = srcImage * mask2[:, :, np.newaxis]
rgbImg = cv2.cvtColor(srcImage, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.imshow(rgbImg)
plt.title('srcImage')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(img)
plt.title('grubCut')
plt.xticks([])
plt.yticks([])

plt.show()
