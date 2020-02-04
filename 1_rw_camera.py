# ==========程序功能：摄像头帧的显示和保存========== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2

cap = cv2.VideoCapture(0)  # 获取摄像头帧流，参数0为摄像头设备索引号

# get()方法获取摄像头帧率和图像尺寸
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)
print(f'fps = {fps}, size={size}')  # f格式适用于Python3.6.8以上，3.6.8以下版本请使用format格式

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 指定视频编解码器
out = cv2.VideoWriter('myCamera.avi', fourcc, fps, size)  # 为构造函数指定视频文件名称
cv2.namedWindow('Camera', 0)
# read()方法获取视频帧
success, frame = cap.read()

while success:    
    cv2.imshow('Camera', frame)
    out.write(frame)
    quitKey = cv2.waitKey(int(1000 / fps))
    if quitKey == (ord('q') or ord('Q')):
        break
    success, frame = cap.read()

cv2.destroyWindow('Camera')
cap.release()
