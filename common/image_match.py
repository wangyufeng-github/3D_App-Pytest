# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2022/8/11 15:37
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : image_match.py
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

import pytesseract
from PIL import ImageChops
from PIL.Image import Image
from aip import AipOcr
import shutil


class ImageMatch:
    def __init__(self):
        pass

    def check_images(self, pathone, filename1, pathtwo, filename2,
                     diffsavename):
        # Check Images ： robot关键字
        """robot自定义关键字: 比较两个长度和宽度一样大的图片【推荐使用】

        :Param pathone: <str> 存放第一个图片的路径，如：Pictures

        :Param filename1: <str> 第一个文件的名字

        :Param pathtwo: <str> 存放第二个图片的路径，如：Desktop

        :Param filename2: <str> 第二个文件的名字

        :Param diffsavename: <str> 图片校验后保存的名称，如：我们不一样

        :Return: <bool> 图片校对结果，True代表无差异，Flase代表有差异

        Example::

        | Check Images | Pictures | before | Desktop | after | 我们不一样 |
        """
        username = self.get_username()
        path_base = '/home/' + str(username) + '/' + str(pathone) + '/' + str(
            filename1) + '.png'
        path_compare = '/home/' + str(username) + '/' + str(
            pathtwo) + '/' + str(filename2) + '.png'
        diff_save_location = '/home/' + str(username) + '/' + str(
            pathtwo) + '/' + str(diffsavename) + '.png'
        image_one = Image.open(path_base)
        image_two = Image.open(path_compare)
        diff = ImageChops.difference(image_one, image_two)
        check_diff = diff.getbbox()
        try:
            if check_diff is None:
                return True
            else:
                diff.save(diff_save_location)
                return False
        except ValueError as e:
            text = ("图片大小和box对应的宽度不一致")
            print("【{0}】{1}".format(e, text))

    def get_image_string(self, path, filename):
        """robot自定义关键字: 提取图片上的信息为字符串

        :Param path: <str> 图片的位置

        :Param filename: <str> 图片的名称

        :Return : <string> 从图片中提取的字符串w

        Example::
        | Get Image String | Desktop | 图片 |
        """
        username = self.get_username()
        path_base = '/home/' + str(username) + '/' + str(path) + '/' + str(
            filename) + '.png'
        text = pytesseract.image_to_string(Image.open(path_base),
                                           lang="chi_sim").replace(
            " ", "").replace("\n", "")
        return text

    def matchImg(self,screenImage,templateImage,confidencevalue=0.7):
        """
        原理：在待检测图像上，从左到右，从上向下计算模板图像与重叠子图像的匹配度，匹配程度越大，两者相同的可能性越大
        模板匹配图片
        :param image:大图
        :param templateImage: 模板图片
        :param confidencevalue: 识别精度
        :return: 字典 包含['rectangle']访问匹配到的图片左顶点图片宽高(left, top, width, height)  ['result']访问匹配到的图片中点 or None


        methods = [cv.TM_SQDIFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_CCOEFF_NORMED]　　#各种匹配算法
        获取的是每种公式中计算出来的值，每个像素点都对应一个值
        min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
        TM_CCOEFF_NORMED：1表示完美匹配,-1表示糟糕的匹配,0表示没有任何相关性(随机序列)
        """
        # 打开模板图片
        screenImage.save(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r'\screenshot\screen.png')
        screenImage = cv.imread(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r'\screenshot\screen.png')
        templateImage = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + f'\image\\template\{templateImage}.png'
        templateImage = cv.imread(templateImage)
        # 调用matchTemplate方法进行匹配
        result = cv.matchTemplate(screenImage, templateImage, cv.TM_CCOEFF_NORMED)
        pos_start = cv.minMaxLoc(result)[3]
        # 匹配对象的中心坐标x y
        x = int(pos_start[0]) + int(templateImage.shape[1] / 2)
        y = int(pos_start[1]) + int(templateImage.shape[0] / 2)
        # 匹配度
        similarity = cv.minMaxLoc(result)[1]
        if similarity < confidencevalue:
            return None
        else:
            return {'result': (x, y),
                    'rectangle': (pos_start[0], pos_start[1], templateImage.shape[1], templateImage.shape[0])}

    def judge_image_exist(self, templateImage, confidencevalue=0.7):
        """
        Judge Image Exist
        判断当前截取的屏幕图片是否能够匹配到模板图片，返回bool值
        """
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image = pyautogui.screenshot()
        image.save(path + r'\screenshot\screen.png')
        obj_image = cv.imread(path + r'\screenshot\screen.png')
        template_path = path + f'\image\\template\{templateImage}.png'
        template = cv.imread(template_path)
        # 调用matchTemplate方法进行匹配
        result = cv.matchTemplate(obj_image, template, cv.TM_CCOEFF_NORMED)
        # 匹配度
        similarity = cv.minMaxLoc(result)[1]
        if similarity < confidencevalue:
            return False
        else:
            return True

    def image_to_click(self, templateImage):
        """
        Image To Click
        根据控件图片名称去操作控件
        """
        img = pyautogui.screenshot()
        ret = self.matchImg(img, templateImage)
        if ret:
            pyautogui.click(ret['result'][0], ret['result'][1], duration=1)
        else:
            print("当前界面无该控件")

    def image_to_right_click(self, templateImage):
        """
        Image To Right Click
        根据控件图片名称去操作控件
        """
        img = pyautogui.screenshot()
        ret = self.matchImg(img, templateImage)
        if ret:
            pyautogui.rightClick(ret['result'][0], ret['result'][1], duration=1)
        else:
            print("当前界面无该控件")

    def image_to_double_click(self, templateImage):
        """
        Image To Right Click
        根据控件图片名称去操作控件
        """
        img = pyautogui.screenshot()
        ret = self.matchImg(img, templateImage)
        if ret:
            pyautogui.doubleClick(ret['result'][0], ret['result'][1], duration=1)
        else:
            print("当前界面无该控件")


if __name__ == '__main__':
    im = ImageMatch()
    im.image_to_click("app_icon")
