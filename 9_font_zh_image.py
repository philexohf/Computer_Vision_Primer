# ===========程序功能：在图片上添加中文============== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import font_zh

srcImg = cv2.imread('./image/test.jpg')
font = font_zh.GetFont('./font/SourceHanSansCN-Light.otf')

ch = '正在前往好莱坞'
position = (100, 100)
text_size = 48
colorBGR = (255, 255, 255)

img = font.draw_text(srcImg, position, ch, text_size, colorBGR)
cv2.namedWindow('image_font_zh', 0)
cv2.imshow('image_font_zh', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
