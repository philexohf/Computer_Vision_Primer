import cv2
import os

path = "./image"
path_temp = "./image_temp"


def bgr2hsv(path):

    file_names = os.listdir(path)

    for file_name in file_names:
        exam_name = file_name[:-4]
        img_type = file_name.split('.')[-1]
        img = cv2.imread(path + '/' + file_name)
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        save_hsv = path + '_' + exam_name + '_HSV' + '.' + img_type
        cv2.imwrite(path_temp + save_hsv, img_hsv)


def bgr2ycrcb(path):
    file_names = os.listdir(path)
    for fileName in file_names:
        exam_name = fileName[:-4]
        img_type = fileName.split('.')[-1]
        img = cv2.imread(path + '/' + fileName)
        img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        save_ycrcb = path + '_' + exam_name + '_YCrCb' + '.' + img_type
        cv2.imwrite(path_temp + save_ycrcb, img_ycrcb)


if __name__ == '__main__':
    bgr2hsv(path)
    bgr2ycrcb(path)
