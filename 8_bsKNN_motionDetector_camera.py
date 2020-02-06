# ==程序功能：用BackgroundSubtractorKNN实现运动目标跟踪== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2

camera = cv2.VideoCapture(0)
bsKNN = cv2.createBackgroundSubtractorKNN(detectShadows=True)
structElement = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 12))


def draw_contours(fn, cnt):
    if cv2.contourArea(cnt) > 1400:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(fn, (x, y), (x + w, y + h), (255, 255, 0), 2)


while True:
    ret, frame = camera.read()
    if not ret:
        break

    fg = bsKNN.apply(frame.copy())  # 计算了前景掩码
    fg_bgr = cv2.cvtColor(fg, cv2.COLOR_GRAY2BGR)
    bw_and = cv2.bitwise_and(fg_bgr, frame)
    draw = cv2.cvtColor(bw_and, cv2.COLOR_BGR2GRAY)
    draw = cv2.GaussianBlur(draw, (21, 21), 0)
    draw = cv2.threshold(draw, 20, 255, cv2.THRESH_BINARY)[1]
    draw = cv2.dilate(draw, structElement, iterations=2)
    # findContours()旧版返回image,contours, hierarchy三个参数,新版返回contours, hierarchy两个参数
    contours, hierarchy = cv2.findContours(draw.copy(),
                                           cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        draw_contours(frame, c)

    cv2.imshow("Motion Detector", frame)

    if cv2.waitKey(int(1000 / 12)) & 0xff == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
