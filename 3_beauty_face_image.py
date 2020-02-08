# =============程序功能：图片美颜程序============== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np
'''
美颜公式
Dest =(Src * (100 - Opacity) + 
(Src + 2 * GuassBlur(EPFFilter(Src) - Src + 128) - 256) * Opacity) /100
'''


def beauty_face(image):
    # para1,para2: 美颜细节的程度
    para1 = 3
    para2 = 1
    p = 0.1
    dx = para1 * 5  # 双边滤波参数
    fc = para1 * 12.5  # 双边滤波参数

    temp1 = cv2.bilateralFilter(image, dx, fc, fc)
    temp2 = cv2.add(cv2.subtract(temp1, image), (10, 10, 10, 128))
    temp3 = cv2.GaussianBlur(temp2, (2*para2 - 1, 2*para2-1), 0)
    temp4 = cv2.add(image, temp3)
    dst = cv2.add(cv2.addWeighted(image, p, temp4, 1 - p, 0.0), (10, 10, 10, 255))

    return dst


img = cv2.imread('./image/face1.png')

beautyFace = beauty_face(img)
beauty = np.hstack([img, beautyFace])

cv2.imshow("beauty face", beauty)
cv2.waitKey(0)

cv2.destroyAllWindows()
