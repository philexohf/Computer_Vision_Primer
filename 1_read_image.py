# ===程序功能：读取image文件夹中的一幅图片并在窗口显示出来=== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2  # 导入OpenCV软件包

img = cv2.imread('./image/lancelot_guinevere.jpg')  # 读取当前目录下的图片.
cv2.namedWindow('img', 0)  # 创建一个窗口，参数0表示窗口大小可改变.
cv2.imshow('img', img)  # 显示图片，第一个参数是显示图像的窗口的名字，第二个参数是要显示的图像.
cv2.waitKey(0)  # 等待键盘触发时间，单位为毫秒，0表示时间为无穷大

cv2.destroyAllWindows()  # 销毁窗口
