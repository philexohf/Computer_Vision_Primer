import cv2


cap = cv2.VideoCapture(0)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('size={}'.format(size))
cv2.namedWindow('camera', 0)
# 读帧
success, frame = cap.read()
while success:
    cv2.imshow('camera', frame)  # 显示
    quitKey = cv2.waitKey(int(1000 / 30))  # 延迟
    if quitKey == (ord('q') or ord('Q')):
        break
    success, frame = cap.read()  # 获取下一帧

cap.release()
