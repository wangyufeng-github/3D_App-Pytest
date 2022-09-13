# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2022/8/29 10:58
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : test_login.py
# @Software : PyCharm
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


@pytest.mark.login
@allure.feature("用户登录模块")
class TestLogin:
    '''
    测试登录界面
    '''

    @allure.title("管理员账号登录测试")
    @allure.severity("critical")
    def test_admin_to_login(self, start_app):
        '''
        1.打开软件，进入登录界面
        2.输入管理员账号和密码
        3.点击登录按钮
        '''
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
        # 点击登录按钮
        LoginPageAction().login_page_login_button_click()
        logger.info("登录界面点击登录按钮，执行登录操作")
        sleep(5)
        try:
            patient_window = auto.StatusBarControl(Name="进入病例管理", Depth=2)
            status = OperateWindow().window_exists(patient_window)
            logger.info("软件登录成功，进入病人管理界面")
        except LookupError as e:
            assert status, "软件登录失败，未成功进入病人数据管理界面"
        finally:
            Tool().stop_application()
            logger.info("软件已退出")

    @allure.title("普通用户账号登录测试")
    @allure.severity("critical")
    def test_user_to_login(self, start_app):
        '''
        1.打开软件，进入登录界面
        2.输入普通用户账号和密码
        3.点击登录按钮
        '''
        username = Tool().get_config("user", "normal_user")
        password = Tool().get_config("user", "normal_password")
        # 点击普通用户按钮
        LoginPageAction().login_page_user_button_click()
        # 点击用户名编辑框
        LoginPageAction().login_page_username_edit_click()
        # 用户名编辑界面输入
        LoginPageAction().login_page_username_edit_sendkeys(username)
        # 点击密码输入框
        LoginPageAction().login_page_password_edit_click()
        # 密码输入框输入
        LoginPageAction().login_page_password_edit_sendkeys(password)
        # 点击登录按钮
        LoginPageAction().login_page_login_button_click()
        logger.info("登录界面点击登录按钮，执行登录操作")
        sleep(5)
        try:
            patient_window = auto.StatusBarControl(Name="进入病例管理", Depth=2)
            status = OperateWindow().window_exists(patient_window)
            logger.info("软件登录成功，进入病人管理界面")
        except LookupError as e:
            assert status, "软件登录失败，未成功进入病人数据管理界面"
        finally:
            Tool().stop_application()
            logger.info("软件已退出")

    @allure.title("技服账号登录测试")
    @allure.severity("critical")
    def test_service_to_login(self, start_app):
        '''
        1.打开软件，进入登录界面
        2.输入技服账号和密码
        3.点击登录按钮
        '''
        username = Tool().get_config("user", "service_name")
        password = Tool().get_config("user", "service_password")
        # 点击技服按钮
        LoginPageAction().login_page_service_button_click()
        # 点击用户名编辑框
        LoginPageAction().login_page_username_edit_click()
        # 用户名编辑界面输入
        LoginPageAction().login_page_username_edit_sendkeys(username)
        # 点击密码输入框
        LoginPageAction().login_page_password_edit_click()
        # 密码输入框输入
        LoginPageAction().login_page_password_edit_sendkeys(password)
        # 点击登录按钮
        LoginPageAction().login_page_login_button_click()
        logger.info("登录界面点击登录按钮，执行登录操作")
        sleep(5)
        try:
            patient_window = auto.StatusBarControl(Name="进入病例管理", Depth=2)
            status = OperateWindow().window_exists(patient_window)
            logger.info("软件登录成功，进入病人管理界面")
        except LookupError as e:
            assert status, "软件登录失败，未成功进入病人数据管理界面"
        finally:
            Tool().stop_application()
            logger.info("软件已退出")

    @allure.title("登录界面退出测试")
    @allure.severity("critical")
    def test_login_out(self, start_app):
        '''
        1.打开软件，进入登录界面
        2.点击退出按钮
        '''
        # 点击登录界面退出按钮
        LoginPageAction().login_page_quit_button_click()
        sleep(2)
        try:
            state = Tool().get_process_state("My3DApp.exe")
        except OSError as e:
            assert state, "程序未退出"
        finally:
            Tool().stop_application()
            logger.info("软件已退出")


if __name__ == '__main__':
    path = Path.cwd().parent.joinpath('reports', 'tmp')
    for file1 in path.glob('*.json'):
        os.remove(file1)
    for file2 in path.glob('*.txt'):
        os.remove(file2)
    for file3 in path.glob('*.png'):
        os.remove(file3)
    for file4 in path.glob('*.attach'):
        os.remove(file4)
    # pytest.main(['-v', 'test_login.py','--alluredir=../reports/tmp'])
    pytest.main(['-v', '../login/test_login.py::TestLogin::test_login_out', '--alluredir=../../reports/tmp'])
    os.system('allure serve ../../reports/tmp')
    # os.system('allure generate ../reports -o ../reports/html --clean')
    # os.system('allure open ../reports/html')
