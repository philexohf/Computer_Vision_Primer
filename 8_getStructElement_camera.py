# ========程序功能：计算帧间差异的目标跟踪========= #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np

camera = cv2.VideoCapture(0)
# 返回指定形状和尺寸的结构元素
structElement = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
kernel = np.ones((5, 5), np.uint8)
background = None

ret, frame = camera.read()

while ret:
    if background is None:
        background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        background = cv2.GaussianBlur(background, (21, 21), 0)
        continue

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    diff = cv2.absdiff(background, gray_frame)  # 得到一个差分图
    diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]  # 固定阈值处理黑白图
    diff = cv2.dilate(diff, structElement, iterations=2)  # 膨胀处理图像

    # findContours()旧版返回image,contours, hierarchy三个参数,新版返回contours, hierarchy两个参数
    contours, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) < 1500:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow("contours", frame)
    cv2.imshow("diff", diff)

    if cv2.waitKey(int(1000 / 12)) & 0xff == ord("q"):
        break

    ret, frame = camera.read()

cv2.waitKey(0)
cv2.destroyAllWindows()
camera.release()
