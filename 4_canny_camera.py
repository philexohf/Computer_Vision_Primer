# =====程序功能：用Canny算子处理摄像头帧的图像效果====== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2

cap = cv2.VideoCapture(0)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
saveImg = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('camera.mp4', saveImg, 30, size)

cv2.namedWindow('camera', 0)
cv2.namedWindow('canny', 0)

success, frame = cap.read()
while success:
    cv2.imshow('camera', frame)
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cannyImg = cv2.Canny(grayImg, 30, 150)
    # out.write(cannyImg)
    cv2.imshow('canny', cannyImg)
    quitKey = cv2.waitKey(int(1000 / 30))
    if quitKey == (ord('q') or ord('Q')):
        break
    success, frame = cap.read()

cv2.destroyAllWindows()
cap.release()
