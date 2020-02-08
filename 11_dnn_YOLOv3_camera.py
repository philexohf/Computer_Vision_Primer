# ====程序功能：基于OpenCV的YOLOv3目标检测程序==== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np

# 初始化参数
conf_threshold = 0.5  # 置信度阈值
nms_threshold = 0.4  # 非极大值抑制(Non-Maximum Suppression, NMS)阈值
input_width = 416  # 输入图像的宽度
input_height = 416  # 输入图像的高度

# 加载分类名称文件
classesFile = "./data/coco.names"  # coco.names文件已存在，不用下载。
# classes = None
with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

# YOLOv3网络文件
modelConfiguration = './data/yolov3-tiny.cfg'
modelWeights = 'D:/DataSets/model/yolov3-tiny.weights'  # .weights文件需要自己下载放入对应文件夹
# 加载网络
model = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
model.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
model.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


# Get the names of the output layers
def get_output_names(net):
    # Get the names of all the layers in the network
    layers_names = net.getLayerNames()
    # Get the names of the output layers,
    # i.e. the layers with unconnected outputs
    return [layers_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]


# 绘制预测边界框
def draw_predict(class_id, conf, left, top, right, bottom):
    cv2.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)
    label = '%.2f' % conf

    # 获取类名及置信度标签
    if classes:
        assert (class_id < len(classes))
        label = '%s:%s' % (classes[class_id], label)

    # 在边界框顶部显示标签
    label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(top, label_size[1])
    cv2.rectangle(frame, (left, top - round(1.5 * label_size[1])),
                  (left + round(1.5 * label_size[0]), top + base_line),
                  (255, 255, 255), cv2.FILLED)
    cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 1)


# 置信度过低时移除边界框
def post_process(frame, outs):
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]
    # Scan through all the bounding boxes output from the network and
    # keep only the ones with high confidence scores.
    # Assign the box's class label as the class with the highest score.
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_threshold:
                center_x = int(detection[0] * frame_width)
                center_y = int(detection[1] * frame_height)
                width = int(detection[2] * frame_width)
                height = int(detection[3] * frame_height)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    # 消除冗余的低置信度重叠框
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        draw_predict(class_ids[i], confidences[i], left, top, left + width, top + height)


winName = 'Object Detector'
# cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cv2.namedWindow(winName, 0)
cap = cv2.VideoCapture(0)

while cv2.waitKey(1) < 0:
    success, frame = cap.read()
    # 视频结束时停止程序
    if not success:
        print('Done')
        cv2.waitKey(3000)
        cap.release()
        break

    # 创建4D blob
    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (input_width, input_height), [0, 0, 0], 1, crop=False)
    # 设置输入给网络
    model.setInput(blob)
    # 前向传播得到输出
    outs = model.forward(get_output_names(model))
    # 低置信度时移除框体
    post_process(frame, outs)
    # 获取处理的总时间
    t, _ = model.getPerfProfile()
    label = 'Inference time: {:.2f} ms'.format(t * 1000.0 / cv2.getTickFrequency())
    cv2.putText(frame, label, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

    cv2.imshow(winName, frame)
