# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np


def color_hist(image, color):
    hist = cv2.calcHist([image],       # 传入图像（列表）
                        [0],           # 使用的通道（使用通道：可选[0],[1],[2]）
                        None,          # 不使用mask
                        [256],         # HistSize
                        [0.0, 255.0])  # 直方图柱的范围
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    hist_img = np.zeros([256, 256, 3], np.uint8)
    hpt = int(0.9 * 256)
    for h in range(256):
        intensity = int(hist[h] * hpt / maxVal)
        cv2.line(hist_img, (h, 256), (h, 256 - intensity), color)
    return hist_img


if __name__ == '__main__':
    original_img = cv2.imread("./image/lancelot_guinevere.jpg")
    img = cv2.resize(original_img, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC)
    b, g, r = cv2.split(img)

    hist_channelB = color_hist(b, [255, 0, 0])
    hist_channelG = color_hist(g, [0, 255, 0])
    hist_channelR = color_hist(r, [0, 0, 255])

    cv2.imshow("hist_B", hist_channelB)
    cv2.imshow("hist_G", hist_channelG)
    cv2.imshow("hist_R", hist_channelR)
    cv2.imshow("img", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
