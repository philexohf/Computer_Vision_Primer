import cv2
import numpy as np
'''
美颜公式
Dest =(Src * (100 - Opacity) + 
(Src + 2 * GuassBlur(EPFFilter(Src) - Src + 128) - 256) * Opacity) /100
'''

img = cv2.imread('./image/xq.jpg')


def beauty_face(img):
    dst = np.zeros_like(img)
    #para1,para2: 美颜细节的程度
    para1 = 3
    para2 = 1
    dx = para1 * 5 # 双边滤波参数
    fc = para1 * 12.5 # 双边滤波参数
    p = 0.1
    
    temp1 = cv2.bilateralFilter(img,dx,fc,fc)
    temp2 = cv2.add(cv2.subtract(temp1,img), (10,10,10,128))
    temp3 = cv2.GaussianBlur(temp2,(2*para2 - 1,2*para2-1),0)
    temp4 = cv2.add(img,temp3)

    dst = cv2.add(cv2.addWeighted(img,p,temp4,1-p,0.0),(10, 10, 10,255))

    return dst


dst = beauty_face(img)
cv2.imshow("src",img)
cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
