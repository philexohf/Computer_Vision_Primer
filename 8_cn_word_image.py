import cv2
import cn_word


srcImg = cv2.imread('test.jpg')
cv2.namedWindow('picture', 0)
cv2.imshow("picture", srcImg)

cnWord = '月亮岛'
position = (100, 100)
text_size = 48
colorBGR = (255, 0, 0)
cnTxt = cn_word.put_chinese_text('SourceHanSansCN-ExtraLight.otf')

dstImg = cnTxt.draw_text(srcImg, position, cnWord, text_size, colorBGR)
cv2.namedWindow('cnWord', 0)
cv2.imshow('cnWord', dstImg)
cv2.imwrite('cnWord.jpg', dstImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
