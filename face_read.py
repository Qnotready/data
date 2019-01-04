#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import cv2
import numpy as np

# cv2.namedWindow("face")
# cap = cv2.VideoCapture(0)  # 加载摄像头录制
# # cap = cv2.VideoCapture("face.mp4") #打开视频文件
# success, frame = cap.read()
# # classifier = cv2.CascadeClassifier("/Users/yuki/anaconda/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml")  # 确保此xml文件与该py文件在一个文件夹下，否则将这里改为绝对路径
#
# # haarcascade_frontalface_default.xml
# classifier = cv2.CascadeClassifier(
#     "F:\\pythoncode\\pythonsafe\\opencv-3.3.0\\data\\haarcascades\\haarcascade_frontalface_default.xml")  # 确保此xml文件与该py文件在一个文件夹下，否则将这里改为绝对路径
#
# while success:
#     success, frame = cap.read()
#     size = frame.shape[:2]
#     image = np.zeros(size, dtype=np.float16)
#     image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.equalizeHist(image, image)
#     divisor = 8
#     h, w = size
#     minSize = (w // divisor, h // divisor)
#     faceRects = classifier.detectMultiScale(image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize)
#     if len(faceRects) > 0:
#         for faceRect in faceRects:
#             x, y, w, h = faceRect
#             cv2.rectangle(frame, (x, y), (x + h, y + w), (0, 255, 0), 2)
#             # 锁定 眼和嘴巴
#     #             cv2.circle(frame, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8), (255, 0, 0))   # 左眼
#     #             cv2.circle(frame, (x + 3 * w //4, y + h // 4 + 30), min(w // 8, h // 8), (255, 0, 0))   #右眼
#     #             cv2.rectangle(frame, (x + 3 * w // 8, y + 3 * h // 4), (x + 5 * w // 8, y + 7 * h // 8), (255, 0, 0))   #嘴巴
#     cv2.imshow("test", frame)
#     key = cv2.waitKey(10)
#     c = chr(key & 255)
#     if c in ['q', 'Q', chr(27)]:
#         break
# cv2.destroyWindow("face")

cv2.namedWindow("Face_Detect")  # 定义一个窗口
cap = cv2.VideoCapture(0)  # 捕获摄像头图像
success, frame = cap.read()  # 读入第一帧

classifier = cv2.CascadeClassifier("F:\\pythoncode\\pythonsafe\\opencv-3.3.0\\data\\haarcascades\\haarcascade_frontalface_alt.xml")
# 定义人脸识别的分类数据集，需要自己查找，在opencv的目录下，参考上面我的路径

while success:  # 如果读入帧正常
    size = frame.shape[:2]
    image = np.zeros(size, dtype=np.float16)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.equalizeHist(image, image)
    divisor = 8
    h, w = size
    minSize = (int(w / divisor), int(h / divisor))  # 像素一定是整数，或者用w//divisor

    faceRects = classifier.detectMultiScale(image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize)
    # 人脸识别

    if len(faceRects) > 0:
        for faceRect in faceRects:
            x, y, w, h = faceRect
            cv2.circle(frame, (x + w // 2, y + h // 2), min(w // 2, h // 2), (255, 0, 0), 2)  # 圆形轮廓
            cv2.circle(frame, (x + w // 4, y + 2 * h // 5), min(w // 8, h // 8), (0, 255, 0), 2)  # 左眼轮廓
            cv2.circle(frame, (x + 3 * w // 4, y + 2 * h // 5), min(w // 8, h // 8), (0, 255, 0), 2)  # 右眼轮廓
            cv2.circle(frame, (x + w // 2, y + 2 * h // 3), min(w // 8, h // 8), (0, 255, 0), 2)  # 鼻子轮廓
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 矩形轮廓

    cv2.imshow("Face_Detect", frame)
    # 显示轮廓
    success, frame = cap.read()  # 如正常则读入下一帧
    key = cv2.waitKey(10)
    c = chr(key & 255)
    if c in ['q', 'Q', chr(27)]:  # 如果键入‘q'退出循环
        print('exit\n')
        break  # 退出循环

    # 循环结束则清零
cap.release()
cv2.destroyAllWindows()