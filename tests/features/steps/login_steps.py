# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2022/8/29 10:58
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : test_login.py
# @Software : PyCharm
import sys
sys.path.append('./')
import os
import sys
from pathlib import Path
import pytest
import allure
import uiautomation as auto
from time import sleep
from common.control_element import OperateWindow
from common.image_match import ImageMatch
from common.log import logger
from common.mouse import CommonOperate
from page.login_page import LoginPage, LoginPageAction
from common.tool import Tool
from common.screen_shot import *
from pytest_bdd import *


@scenario("../tests/login.feature",scenario_name="Enter the username and password to log in using the admini")

@given("open the application")
@allure.step("任务栏打开软件")
def start_app():
    ImageMatch().image_to_click("app_icon")
    time.sleep(10)
    login_state = Tool().get_process_state("My3DApp")
    if login_state:
        logger.info("软件成功启动")
    else:
        print("未获取到后台进程，请检查程序是否启动")
        logger.info("软件启动失败")

@when("input username and password")
@allure.step("管理员账号输入用户名和密码")
def input_username_and_password():
    username = Tool().get_config("user", "admin_user")
    password = Tool().get_config("user", "admin_password")
    # 登录界面点击管理员按钮
    LoginPageAction().login_page_admin_button_click()
    # 点击用户名输入框
    LoginPageAction().login_page_username_edit_click()
    # 用户名编辑界面输入
    LoginPageAction().login_page_username_edit_sendkeys(username)
    # 点击密码输入框
    LoginPageAction().login_page_password_edit_click()
    # 密码输入框输入
    LoginPageAction().login_page_password_edit_sendkeys(password)

@when("click login button")
@allure.step("点击登录按钮")
def click_login_button():
    LoginPageAction().login_page_login_button_click()
    logger.info("登录界面点击登录按钮，执行登录操作")
    sleep(5)

@then("assert login status and close application")
@allure.step("判断是否进入登录界面")
def assert_login():
    try:
        patient_window = auto.StatusBarControl(Name="进入病例管理", Depth=2)
        status = OperateWindow().window_exists(patient_window)
        logger.info("软件登录成功，进入病人管理界面")
    except LookupError as e:
        assert status, "软件登录失败，未成功进入病人数据管理界面"
    finally:
        Tool().stop_application()
        logger.info("软件已退出")


if __name__ == '__main__':
    # path = Path.cwd().parent.joinpath('reports', 'tmp')
    # for file1 in path.glob('*.json'):
    #     os.remove(file1)
    # for file2 in path.glob('*.txt'):
    #     os.remove(file2)
    # for file3 in path.glob('*.png'):
    #     os.remove(file3)
    # for file4 in path.glob('*.attach'):
    #     os.remove(file4)
    # pytest.main(['-v', 'test_login.py','--alluredir=../reports/tmp'])
    # pytest.main(['-v', '../tests/login_steps.py', '--alluredir=../../reports/tmp'])
    # os.system('allure serve ../../reports/tmp')
    # os.system('allure generate ../reports -o ../reports/html --clean')
    # os.system('allure open ../reports/html')
    print(os.getcwd())