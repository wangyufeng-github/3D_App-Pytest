# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2022/8/11 14:51
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : mouse.py
# @Software : PyCharm



from ast import Return
import getpass
import pyautogui
import os
import sys
import subprocess
import random
import glob
import cv2 as cv
# import pandas as pd
from time import sleep
from time import time
from aip import AipOcr
import shutil


class CommonOperate:
    def __init__(self):
        # 保护措施，避免失控
        pyautogui.FAILSAFE = False
        # 为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。
        pyautogui.PAUSE = 0.5

    def get_current_location(self):
        """robot自定义关键字: 获取当前鼠标位置

        :Return: <int> 当前鼠标位置(如：500, 500)

        Example::

        | Get Current Location |
        """
        position_x, position_y = pyautogui.position()
        print(f'position_x={position_x} position_y={position_y}')
        return position_x, position_y

    def mouse_absolute_move(self, position_x, position_y):
        """robot自定义关键字: 移动鼠标到指定位置(绝对位移)

        :Param position_x: <int> 移动到指定位置横向坐标

        :Param position_y: <int> 移动到指定位置纵向坐标

        :Return: None

        Example::

        | Mouse Absolute Move | 50 | 50 |
        """
        pyautogui.moveTo(int(position_x),
                         int(position_y),
                         duration=1,
                         tween=pyautogui.linear)

    def mouse_left_click(self):
        """robot自定义关键字: 单击鼠标左键

        :Return: None

        Example::

        | Mouse Left Click |
        """
        pyautogui.click(x=None,
                        y=None,
                        clicks=1,
                        interval=0.0,
                        button='left',
                        duration=0.0,
                        tween=pyautogui.linear)

    def mouse_right_click(self):
        """robot自定义关键字: 单击鼠标右键

                :Return: None

                Example::

                | Mouse Right Click |
        """
        pyautogui.rightClick()

    def mouse_move_left_click(self, position_x, position_y):
        """鼠标移动到指定位置并左击

        :Param position1_x: <int> 起始位置横向坐标

        :Param position1_y: <int> 起始位置纵向坐标

        :Return: None

        Example::

        | Mouse Move Left Click | 10 | 100 |
        """
        CommonOperate.mouse_absolute_move(self, position_x, position_y)
        CommonOperate.mouse_left_click(self)

    def mouse_middle_click(self):
        """robot自定义关键字: 单击鼠标滚轴中键

        :Return: None

        Example::

        | Mouse Middle Click |
        """
        pyautogui.middleClick()

    def mouse_double_click(self):
        """robot自定义关键字: 双击鼠标左键

        :Return: None

        Example::

        | Mouse Double Click |
        """
        pyautogui.doubleClick(x=None,
                              y=None,
                              interval=0.1,
                              button='left',
                              duration=0.0,
                              tween=pyautogui.linear)

    def mouse_down(self):
        """robot自定义关键字: 按住鼠标左键(按住不放)

        :Return: None

        Example::

        | Mouse Down |
        """
        pyautogui.mouseDown(button='left')

    def mouse_up(self):
        """robot自定义关键字: 松开鼠标左键

        :Return: None

        Example::

        | Mouse Up |
        """
        pyautogui.mouseUp(button='left')

    def input_message(self, info):
        """robot自定义关键字: 按照0.5秒输入一个字符的频率输入字符串信息

        :Param info: <str> 需要输入的字符串信息

        :Return: None

        Example::

        | Input Message | hello uos |
        """
        pyautogui.typewrite(message=info, interval=0.2)

    def press_key(self, keyname):
        """robot自定义关键字: 键盘按键操作

        :Param keyname: <str> 键盘上指定的按键

        :Return: None

        Example::

        | Press Key | down |
        """
        pyautogui.press(keyname)

    def press_key_down(self, keyname):
        """robot自定义关键字: 按住键盘按键不放

        :Param keyname: <str> 键盘上指定的按键

        :Return: None

        Example::

        | Press Key Down| ctrl |
        """
        pyautogui.keyDown(keyname)

    def press_key_up(self, keyname):
        """robot自定义关键字: 松开键盘按键

        :Param keyname: <str> 键盘上指定的按键

        :Return: None

        Example::

        | Press Key Up | alt |
        """
        pyautogui.keyUp(keyname)

    def hot_key(self, *args):
        """robot自定义关键字: 键盘热键操作

        :Param args: <str> 键盘上指定的按键,这里实现自动识别多个按键功能

        :Return: None

        Example::

        | Hot Key | ctrl | alt | a |
        """
        if len(args) == 2:
            pyautogui.hotkey(args[0], args[1])
        elif len(args) == 3:
            pyautogui.hotkey(args[0], args[1], args[2])
        else:
            print('Your input is wrong. Please input the correct number of parameters')

    def screen_shot_all(self, image_path):
        """
        截取全屏
        :param image_path:图像完整路径，包含图片名称
        :return:
        """
        pyautogui.screenshot(image_path)

    def screen_shot_part(self, position_x1, position_y1, position_x2, position_y2, image_path):
        """
        根据坐标位置截取图像
        :param position_x1:
        :param position_y1:
        :param position_x2:
        :param position_y2:
        :param image_path:
        :return:
        """
        im = pyautogui.screenshot(region=(position_x1, position_y1, position_x2, position_y2))
        im.save(image_path)


if __name__ == '__main__':
    m = CommonOperate()
