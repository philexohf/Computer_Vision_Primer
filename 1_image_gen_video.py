# ===程序功能：将image文件夹中的所有图片合并成一个视频文件=== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import os


# 图像生成器，对生成器不熟悉的同学自己查看Python生成器的内容
def read_image():
    img_dir = './image/'
    img_list = os.listdir(img_dir)
    for i in img_list:
        path = img_dir + i
        print(path)
        yield path


fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 指定视频编解码器
out = cv2.VideoWriter('genVideo.mp4', fourcc, 1.0, (960, 720), True)  # 为构造函数指定视频文件名称

for item in read_image():
    img = cv2.imread(item)  # 读取当前目录下的图片.
    dstImg = cv2.resize(img, (960, 720))
    out.write(dstImg)
    cv2.imshow('dstImg', dstImg)  # 显示图片，第一个参数是显示图像的窗口的名字，第二个参数是要显示的图像.
    cv2.waitKey(100)

cv2.destroyAllWindows()
