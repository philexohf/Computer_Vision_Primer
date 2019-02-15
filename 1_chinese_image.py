import cv2
import cn_txt

img = cv2.imread('test.jpg')

line = '月亮岛'
pos = (100, 100)
text_size = 48
colorBGR = (255, 0, 0)
cnTxt = cn_txt.put_chinese_text('Monaco Yahei.ttf')

image = cnTxt.draw_text(img, pos, line, text_size, colorBGR)
cv2.namedWindow('image', 0)
cv2.imshow('image', image)
cv2.imwrite('yld.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
