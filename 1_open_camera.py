import cv2


videoCapture = cv2.VideoCapture(0)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('size={}'.format(size))
cv2.namedWindow('camera', 0)
# 读帧
success, frame = videoCapture.read()
while success:
    cv2.imshow('camera', frame)  # 显示
    qKey = cv2.waitKey(int(1000 / 30))  # 延迟
    if qKey == (ord('q') or ord('Q')):
        break
    success, frame = videoCapture.read()  # 获取下一帧

videoCapture.release()
