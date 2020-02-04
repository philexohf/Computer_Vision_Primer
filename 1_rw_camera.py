# ==========程序功能：摄像头帧的显示和保存========== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2

cap = cv2.VideoCapture(0)  # 获取摄像头帧流，参数0为摄像头设备索引号

fps = 30  # 因为get()方法不能返回摄像头的帧率，所以设置为固定值30
# get()方法获取摄像头帧的尺寸
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)
print('size={}'.format(size))

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 指定视频编解码器
out = cv2.VideoWriter('myCamera.avi', fourcc, fps, size)  # 为构造函数指定视频文件名称
cv2.namedWindow('camera', 0)
# 读帧
success, frame = cap.read()

while success:    
    cv2.imshow('camera', frame)  # 显示
    out.write(frame)
    quitKey = cv2.waitKey(int(1000 / fps))  # 延迟
    if quitKey == (ord('q') or ord('Q')):
        break
    success, frame = cap.read()  # read()方法获取视频帧

cv2.destroyWindow('camera')
cap.release()
