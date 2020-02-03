# ==========程序功能：读取视频文件并按帧率播放========= #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2

path = "D:/DataSets/VideoDataSets"  # 视频文件存放的绝对路径
cap = cv2.VideoCapture(path + 'Paris.mp4')  # Paris.mp4改成你自己的文件名

# 使用get()方法获取视频帧率fps及图像尺寸size
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('fps={}, size={}'.format(fps, size))

cv2.namedWindow('testVideo', 0)  # 创建窗口
# read()方法获取视频帧，获取失败的情况下read()方法会返回参数(false, None)
success, frame = cap.read()

while success:
    cv2.imshow('testVideo', frame)
    quitKey = cv2.waitKey(int(1000 / fps))
    if quitKey == (ord('q') or ord('Q')):  # Python标准函数ord()可将字符转换成ASCII码
        break
    success, frame = cap.read()

cv2.destroyWindow('testVideo')  # 销毁窗口
cap.release()
