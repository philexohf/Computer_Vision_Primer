# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import random
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_alt2.xml')
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
text = "Camera"
cv2.namedWindow('Camera')
while True:
    success, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (random.randint(0, 255),
                                                  random.randint(0, 255),
                                                  random.randint(0, 255)),
                      3, cv2.LINE_AA)
    AddText = frame.copy()
    cv2.putText(AddText, text, (60, 100), cv2.FONT_HERSHEY_COMPLEX, 1.0, (100, 200, 200), 3)

    # 将原图片和添加文字后的图片拼接起来
    res = np.hstack([frame, AddText])
    cv2.imshow("Camera", res)
    cv2.waitKey(int(1000 / fps))
