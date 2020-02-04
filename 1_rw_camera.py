# ==========程序功能：摄像头帧的显示和保存========== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2

cap = cv2.VideoCapture(0)  # 获取摄像头帧流，参数0为摄像头设备索引号

# 使用get()方法获取摄像头的帧率和图像的尺寸
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)
print(f'fps = {fps}, size = {size}')  # Python3.6.8以上版本适用f""格式,以下请使用format格式

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 指定视频编解码器
out = cv2.VideoWriter('myCamera.avi', fourcc, fps, size)  # 为构造函数指定视频文件名称

cv2.namedWindow('camera', 0)
# read()方法读取图像帧
success, frame = cap.read()

while success:    
    cv2.imshow('camera', frame)
    out.write(frame)
    quitKey = cv2.waitKey(int(1000 / fps))
    if quitKey == (ord('q') or ord('Q')):
        break
    success, frame = cap.read()

cv2.destroyWindow('camera')
cap.release()
