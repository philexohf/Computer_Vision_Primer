# ===程序功能：用Canny算子处理视频图像并添加中文logo=== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import font_zh

line = '计算机视觉'
position = (100, 100)
text_size = 100
colorBGR = (255, 0, 0)
cnTxt = font_zh.GetFont('./font/SourceHanSansCN-Light.otf')
cap = cv2.VideoCapture('D:/DataSets/VideoDataSets/Paris.mp4')  # 改成你自己的视频文件路径
# 获得码率及尺寸
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('fps={}, size={}'.format(fps, size))
# saveImage = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.mp4', saveImage, fps, size)
cv2.namedWindow('Video', 0)
cv2.namedWindow('dstVideo', 0)
# 读帧
success, frame = cap.read()

while success:
    cv2.imshow('Video', frame)
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cannyImage = cv2.Canny(grayImage, 30, 150)
    dst = cv2.bitwise_and(frame, frame, mask=cannyImage)
    cndst = cnTxt.draw_text(dst, position, line, text_size, colorBGR)
    cv2.imshow('dstVideo', cndst)
    # out.write(cndst)
    quitKey = cv2.waitKey(int(1000 / fps))
    if quitKey == (ord('q') or ord('Q')):
        break
    success, frame = cap.read()  # 获取下一帧

cv2.destroyAllWindows()
cap.release()
