import cv2
import font_zh

srcImg = cv2.imread('./image/test.jpg')
ch = '月亮岛'
font = font_zh.GetFont('./font/SourceHanSansCN-Light.otf')
dstImg = font.draw_text(srcImg, (100, 100), ch, 48, (255, 0, 0))
cv2.namedWindow('cnWord', 0)
cv2.imshow('cnWord', dstImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
