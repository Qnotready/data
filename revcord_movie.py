#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np
import cv2
from mss import mss
from PIL import ImageGrab
import threading

p = ImageGrab.grab()#获得当前屏幕
k=np.zeros((200,200),np.uint8)
a,b=p.size#获得当前屏幕的大小
fourcc = cv2.VideoWriter_fourcc(*'XVID')#编码格式
video = cv2.VideoWriter('test.avi', fourcc, 16, (a, b))

def inmovie():
    while True:
        im=ImageGrab.grab()
        imm=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
        video.write(imm)
        cv2.imshow('imm', k)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def removie():
    cap = cv2.VideoCapture("F:\\pythoncode\\pythonsafe\\test.avi")
    bs = cv2.createBackgroundSubtractorKNN(detectShadows=True)
    #设置颜色区间
    #白色：0 0 221,180 30 255
    #蓝色：100 43 46,124 255 255
    lower_white = np.array([78,25,221])
    upper_white = np.array([125,99,255])

    while (cap != 0):
        ret, frame = cap.read()
        fgmask = bs.apply(frame)
        th = cv2.threshold(fgmask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
        dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)
        image, content, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in content:
            if cv2.contourArea(c) > 1600:
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv2.imshow("mog", fgmask)
        # cv2.imshow("thresh", th)
        cv2.imshow("detection", frame)

        # q键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



def main():
    th=threading.Thread(inmovie())
    #tj=threading.Thread(removie())
    th.start()
    #tj.start()
    th.join()
    #tj.join()
    video.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()