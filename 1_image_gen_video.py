import cv2
import os

fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # 指定视频编解码器
out = cv2.VideoWriter('video_gen.mp4', fourcc, 1.0, (960, 720), True)  # 为构造函数指定视频文件名称


# 图像生成器，对生成器不熟悉的同学自己查看Python生成器的内容
def read_image():
    img_dir = './image/'
    img_list = os.listdir(img_dir)
    for i in img_list:
        path = img_dir + i
        print(path)
        yield path


for item in read_image():
    img = cv2.imread(item)  # 读取当前目录下的图片.
    img_resize = cv2.resize(img, (960, 720))
    out.write(img_resize)
    cv2.imshow('img', img_resize)  # 显示图片，第一个参数是显示图像的窗口的名字，第二个参数是要显示的图像.
    cv2.waitKey(1000)

cv2.destroyAllWindows()
