import cv2
import os


# 图像生成器
def read_image():
    img_dir = './image/'
    img_list = os.listdir(img_dir)
    for i in img_list:
        path = img_dir + i
        yield path


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('my.mp4', fourcc, 5.0, (960, 720), True)

for item in read_image():
    img = cv2.imread(item)  # 读取当前目录下的图片.
    img_resize = cv2.resize(img, (960, 720))
    out.write(img_resize)
    cv2.imshow('img', img_resize)  # 显示图片，第一个参数是显示图像的窗口的名字，第二个参数是要显示的图像.
    cv2.waitKey(30)

cv2.destroyAllWindows()
