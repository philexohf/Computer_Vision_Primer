import cv2

# 获得视频的格式
videoCapture = cv2.VideoCapture('ow_reunion.mp4')

# 获得码率及尺寸
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print('fps={}, size={}'.format(fps, size))
cv2.namedWindow('mp4', 0)
# 读帧
success, frame = videoCapture.read()
while success:
    cv2.imshow('mp4', frame)  # 显示
    qKey = cv2.waitKey(int(1000 / fps))  # 延迟
    if qKey == (ord('q') or ord('Q')):
        break
    success, frame = videoCapture.read()  # 获取下一帧

videoCapture.release()
