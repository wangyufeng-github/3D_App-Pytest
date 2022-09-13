# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2022/8/9 15:00
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : screen_shot.py
# @Software : PyCharm
import time
import pyautogui
import uiautomation


def save_screenshot(Windows):
    """
    调用uiautomation模块的截图功能
    :param Windows:窗口对象
    :return:
    """
    # 获取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 图片存放路径
    pic_path = "../screenshot/" + now + '_screen.png'
    Windows.CaptureToImage(savePath=pic_path)






