# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2022/8/11 16:20
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : conftest.py
# @Software : PyCharm
import sys
import time

import allure
import pytest
import os, subprocess, uiautomation
from time import sleep
from common.log import logger
import pyautogui
from common.image_match import ImageMatch
from common.control_element import OperateWindow
from common.tool import Tool
from py._xmlgen import html

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1
uiautomation.uiautomation.DEBUG_SEARCH_TIME = True
uiautomation.uiautomation.SetGlobalSearchTimeout(1)


@pytest.fixture(scope="function")
def start_app():
    """
    通过将软件快捷方式增加到dock栏，利用图像识别方式打开软件
    :return:
    """
    ImageMatch().image_to_click("app_icon")
    time.sleep(10)
    login_state = Tool().get_process_state("My3DApp")
    if login_state:
        logger.info("软件成功启动")
    else:
        print("未获取到后台进程，请检查程序是否启动")
        logger.info("软件启动失败")
    # yield
    # patient_window = uiautomation.StatusBarControl(Name="进入病例管理", Depth=2)
    # status = OperateWindow().window_exists(patient_window)
    # if status:
    #     patient_window.CheckBoxControl(searchDepth=3, foundIndex=8).Click()
    # else:
    # os.system("taskkill /im My3DApp.exe -f")
    # sleep(2)


def _capture_screenshot():
    """
    截图函数
    :param func_name:
    :return:
    """
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    pic_path = "../screenshot/" + now + '_screen.png'
    im1 = pyautogui.screenshot()
    im1.save(pic_path)
    return pic_path


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        image_path = _capture_screenshot()
        allure.attach.file(image_path, attachment_type=allure.attachment_type.PNG)
