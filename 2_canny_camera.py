import cv2

# 获得视频的格式
cap = cv2.VideoCapture(0)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
saveImage = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.mp4', saveImage, 30, size)

cv2.namedWindow('camera', 0)
cv2.namedWindow('cannyImage', 0)
# 读帧
success, frame = cap.read()
while success:
    cv2.imshow('camera', frame)  # 显示
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cannyImage = cv2.Canny(grayImage, 30, 150)
    dst = cv2.bitwise_and(frame, frame, mask=cannyImage)
    cv2.imshow('cannyImage', dst)
    out.write(dst)
    qKey = cv2.waitKey(int(1000 / 30))  # 延迟
    if qKey == (ord('q') or ord('Q')):
        break
    success, frame = cap.read()  # 获取下一帧

cap.release()
