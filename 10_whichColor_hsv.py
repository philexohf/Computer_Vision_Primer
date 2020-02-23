import cv2
import numpy as np
import collections


# 定义字典存放颜色分量上下限：{颜色: [lower, upper]}
def get_color_list():
    dict_color = collections.defaultdict(list)

    # 黑色
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 46])
    color_list = list()
    color_list.append(lower_black)
    color_list.append(upper_black)
    dict_color['black'] = color_list

    # 白色
    lower_white = np.array([0, 0, 221])
    upper_white = np.array([180, 30, 255])
    color_list = list()
    color_list.append(lower_white)
    color_list.append(upper_white)
    dict_color['white'] = color_list

    # 红色1
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    color_list = list()
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict_color['red1'] = color_list

    # 红色2
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    # color_list = list()
    # color_list.append(lower_red)
    # color_list.append(upper_red)
    color_list = [lower_red, upper_red]
    dict_color['red2'] = color_list

    # 橙色
    lower_orange = np.array([11, 43, 46])
    upper_orange = np.array([25, 255, 255])
    color_list = list()
    color_list.append(lower_orange)
    color_list.append(upper_orange)
    dict_color['orange'] = color_list

    # 黄色
    lower_yellow = np.array([26, 43, 46])
    upper_yellow = np.array([34, 255, 255])
    color_list = list()
    color_list.append(lower_yellow)
    color_list.append(upper_yellow)
    dict_color['yellow'] = color_list

    # 绿色
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    color_list = list()
    color_list.append(lower_green)
    color_list.append(upper_green)
    dict_color['green'] = color_list

    # 青色
    lower_cyan = np.array([78, 43, 46])
    upper_cyan = np.array([99, 255, 255])
    color_list = list()
    color_list.append(lower_cyan)
    color_list.append(upper_cyan)
    dict_color['cyan'] = color_list

    # 蓝色
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])
    color_list = list()
    color_list.append(lower_blue)
    color_list.append(upper_blue)
    dict_color['blue'] = color_list

    # 紫色
    lower_purple = np.array([125, 43, 46])
    upper_purple = np.array([155, 255, 255])
    color_list = list()
    color_list.append(lower_purple)
    color_list.append(upper_purple)
    dict_color['purple'] = color_list

    return dict_color


# 识别图片颜色
def get_hsv_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    max_value = -100
    color = None
    color_dict = get_color_list()
    for _ in color_dict:
        mask = cv2.inRange(hsv, color_dict[_][0], color_dict[_][1])
        cv2.imwrite('./temp/' + _ + '.jpg', mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        binary = cv2.dilate(binary, None, iterations=2)
        contours, hierarchy = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        sum_value = 0
        for cont in contours:
            sum_value += cv2.contourArea(cont)
        if sum_value > max_value:
            max_value = sum_value
            color = _

    return color


if __name__ == '__main__':
    img = cv2.imread('./image/summer.png')
    print(f'图片的颜色为：{get_hsv_color(img)}')
