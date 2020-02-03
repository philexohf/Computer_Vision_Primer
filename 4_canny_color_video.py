# =====程序功能：用Canny算子检测视频图像的物体边缘====== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2

cap = cv2.VideoCapture('D:/DataSets/VideoDataSets/Paris.mp4')  # 改成你自己的视频文件路径
# 获得码率及尺寸
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('fps={}, size={}'.format(fps, size))
# saveImage = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.mp4', saveImage, fps, size)
cv2.namedWindow('video', 0)
cv2.namedWindow('canny', 0)

success, frame = cap.read()

while success:
    cv2.imshow('video', frame)
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cannyImg = cv2.Canny(grayImg, 50, 150)
    dstImg = cv2.bitwise_and(frame, frame, mask=cannyImg)
    cv2.imshow('canny', dstImg)
    # out.write(dstImg)
    quitKey = cv2.waitKey(int(1000 / fps))
    if quitKey == (ord('q') or ord('Q')):
        break
    success, frame = cap.read()  # 获取下一帧

cv2.destroyAllWindows()
cap.release()
