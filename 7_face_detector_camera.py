# =================程序功能：人脸检测=============== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2

cap = cv2.VideoCapture(0)
# 导入haar分类器文件
face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_alt2.xml')
# 使用get()方法获取摄像头帧率、图像尺寸等参数
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f'fps = {fps}, size = {width, height}, count = {count}')

text = "Face Detector"
color = (0., 255., 0)
cv2.namedWindow('Camera')
success, frame = cap.read()

while success:
    grayImg = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    grayImg = cv2.equalizeHist(grayImg)
    faces = face_cascade.detectMultiScale(grayImg, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2, cv2.LINE_AA)
 
    cv2.putText(frame, text, (60, 100), cv2.FONT_HERSHEY_COMPLEX, 1.0, color, 2)

    cv2.imshow('Camera', frame)
    cv2.waitKey(int(1000 / fps))

    success, frame = cap.read()

cv2.destroyWindow('Camera')
cap.release()
