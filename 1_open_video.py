import cv2

path = "D:/PycharmProjects/Test/"  # 视频文件存放的绝对路径
cap = cv2.VideoCapture(path + 'ow_reunion.mp4')
# 获得码率及尺寸
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('fps={}, size={}'.format(fps, size))
cv2.namedWindow('testVideo', 0)

success, frame = cap.read()
while success:
    cv2.imshow('testVideo', frame)
    quitKey = cv2.waitKey(int(1000 / fps))
    if quitKey == (ord('q') or ord('Q')):
        break
    success, frame = cap.read()

cap.release()
