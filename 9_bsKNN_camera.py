# ========程序功能：BackgroundSubtractor的使用========= #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2

camera = cv2.VideoCapture(0)
bsKNN = cv2.createBackgroundSubtractorKNN(detectShadows=True)

ret, frame = camera.read()

while ret:
    fgMask = bsKNN.apply(frame)
    th = cv2.threshold(fgMask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
    th = cv2.erode(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)
    dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 3)), iterations=2)
    # findContours()旧版返回image,contours, hierarchy三个参数,新版返回contours, hierarchy两个参数
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) > 1000:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow("mog", fgMask)
    cv2.imshow("thresh", th)
    cv2.imshow("diff", frame & cv2.cvtColor(fgMask, cv2.COLOR_GRAY2BGR))
    cv2.imshow("detection", frame)

    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break

    ret, frame = camera.read()

cv2.destroyAllWindows()
camera.release()
