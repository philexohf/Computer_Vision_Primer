# ========程序功能：基于CAMShift的目标跟踪========= #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
# 设置窗口的初始位置
c, r, w, h = 400, 300, 300, 200
trackWindow = (c, r, w, h)
roi = frame[r: r + h, c: c + w]
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# 设定阈值
lower_channel = np.array((100., 30., 32.))
upper_channel = np.array((180., 120., 255.))
# 根据阈值构建掩模
mask = cv2.inRange(hsv, lower_channel, upper_channel)
hist = cv2.calcHist([hsv], [0], mask, [180], [0, 180])
cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
termCriteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], hist, [0, 180], 1)
        # 得到新窗口位置
        ret, trackWindow = cv2.CamShift(dst, trackWindow, termCriteria)
        # 将窗口绘制在图像上
        pts = np.int0(cv2.boxPoints(ret))
        dstImg = cv2.polylines(frame, [pts], True, 255, 2)

        cv2.imshow('dstImg', dstImg)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    else:
        break

cv2.destroyAllWindows()
cap.release()
