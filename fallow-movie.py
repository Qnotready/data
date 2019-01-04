#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import cv2
import numpy as np

cap = cv2.VideoCapture("F:\\pythoncode\\pythonsafe\\test.avi")
result = cap.isOpened()
if result is True:
    while True:
        # 获取每一帧调用camera.read()为我们返回一个2元组。
        # 元组的第一个值是grabbed，表明是否成功从缓冲中读取了frame。
        # 元组的第二个值就是frame它本身。
        ret, image = cap.read()
        if ret is False:
            break
        # 转换到 HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # 设定黑色的阈值
        lower = np.array([0, 0, 0])
        upper = np.array([80, 80, 80])  # 黑色的阙值

        # 腐蚀操作
        mask = cv2.inRange(hsv, lower, upper)
        # 膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点
        mask = cv2.erode(mask, None, iterations=2)
        # 膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点
        mask = cv2.dilate(mask, None, iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        # 初始化瓶盖圆形轮廓质心
        center = None
        # 如果存在轮廓
        if len(cnts) > 0:
            # 找到面积最大的轮廓
            c = max(cnts, key=cv2.contourArea)
            # 确定面积最大的轮廓的外接圆
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            # 计算轮廓的矩
            M = cv2.moments(c)
            # 计算质心
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(image, center, 5, (0, 0, 255), -1)
       # 根据阈值构建掩模
       # 对原图像和掩模进行位运算
        res = cv2.bitwise_and(image, image, mask=mask)
        cv2.imshow('image', image)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        # cv2.waitKey(0)
        k = cv2.waitKey(5) & 0xff
        if k == ord('q'):
            break
    cv2.destroyAllWindows()
    cap.release()
else:
    print("打开失败")