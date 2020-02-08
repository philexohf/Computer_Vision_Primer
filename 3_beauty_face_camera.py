import cv2
import numpy as np
'''
美颜公式
Dest =(Src * (100 - Opacity) + 
(Src + 2 * GuassBlur(EPFFilter(Src) - Src + 128) - 256) * Opacity) /100
'''


def beauty_face(img):
    dst = np.zeros_like(img)
    #para1,para2: 美颜细节的程度
    para1 = 3
    para2 = 1
    dx = para1 * 5 # 双边滤波参数之一 
    fc = para1 * 12.5 # 双边滤波参数之一 
    p = 0.1
   
    temp1 = cv2.bilateralFilter(img,dx,fc,fc)
    temp2 = cv2.add(cv2.subtract(temp1,img), (10,10,10,128))
    temp3 = cv2.GaussianBlur(temp2,(2*para2 - 1,2*para2-1),0)
    temp4 = cv2.add(img,temp3)

    dst = cv2.add(cv2.addWeighted(img,p,temp4,1-p,0.0),(10, 10, 10,255))

    return dst


cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 指定视频编解码器
# out = cv2.VideoWriter('myCamera.avi', fourcc, fps, size)  # 为构造函数指定视频文件名称

success, frame = cap.read()

while success:   
    cv2.imshow('camera', frame)
    dst = beauty_face(frame)
    cv2.imshow('beauty_face',dst)
    # out.write(dst)
    quitKey = cv2.waitKey(30)
    if quitKey == (ord('q') or ord('Q')):
        break
    success, frame = cap.read()

cv2.destroyAllWindows()
cap.release()
