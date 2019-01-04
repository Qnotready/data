#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 文字转语音
import pyttsx3

eagine = pyttsx3.init()  # 初始化语音库，只需要初始化一次

def display():
    print("--" * 30)
    print("1.选择文字转语音")
    print("2.选择退出系统")
    print("--" * 30)


def keybord():
    keyInfo = input("请输入选择选项：\n")
    return keyInfo


def voice():
    sayinfo = input("请输入你需要转语音的文字：\n")
    eagine.say(sayinfo)  # pyttsx3翻译成语音的内容
    eagine.runAndWait()


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
