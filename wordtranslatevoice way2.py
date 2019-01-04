#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import win32com.client
import winsound

def display():
    print("--" * 30)
    print("1.选择文字转语音")
    print("2.选择退出系统")
    print("--" * 30)

def keybord():
    keyInfo = input("请输入选择选项：\n")
    return keyInfo

def voice():
    str = input("请输入你想要转语音的文字：\n")
    speaks = win32com.client.Dispatch("SAPI.SpVoice")
    winsound.Beep(2015, 500)  # 第二个参数为毫秒 应用很广
    speaks.Speak(str)

key = 0


def main():
    while True:
        # input()
        display()
        global key
        try:
            key = int(keybord())
        except ValueError:
            print("请重新输入数字!!!!\n")
        if key == 1:
            voice()
        elif key == 2:
            break
        else:
            print("请输入选项：")

if __name__ == '__main__':
    main()