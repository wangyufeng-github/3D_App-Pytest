# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2022/8/25 8:58
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : login_page.py
# @Software : PyCharm

import time
import uiautomation as auto
from common.control_element import OperateWindow
auto.uiautomation.SetGlobalSearchTimeout(2)

class LoginPage:
    """
    登录界面元素定位类
    """

    def __init__(self):
        self.login_window = auto.WindowControl(Name="My3DApp",Depth=1)

    def login_page_shutdown_button(self):
        """
        登录界面关机按钮
        :return:
        """
        return self.login_window.ButtonControl(foundIndex=1)

    def login_page_username_edit(self):
        """
        登录界面用户名编辑框
        :return:
        """
        return self.login_window.EditControl(foundIndex=1)

    def login_page_password_edit(self):
        """
        登录界面密码输入框
        :return:
        """
        return self.login_window.EditControl(foundIndex=2)

    def login_page_admin_button(self):
        """
        登录界面管理员按钮
        :return:
        """
        return self.login_window.RadioButtonControl(Name="管理员")

    def login_page_user_button(self):
        """
        登录界面用户按钮
        :return:
        """
        return self.login_window.RadioButtonControl(Name="普通用户")

    def login_page_service_button(self):
        """
        登录界面技服按钮
        :return:
        """
        return self.login_window.RadioButtonControl(Name="技服")

    def login_page_login_button(self):
        """
        登录界面登录按钮
        :return:
        """
        return self.login_window.ButtonControl(Name="登录")

    def login_page_quit_button(self):
        """
        登录界面退出按钮
        :return:
        """
        return self.login_window.ButtonControl(Name="退出")


class LoginPageAction(LoginPage):
    """
    登录界面操作类
    """

    def __init__(self):
        super(LoginPageAction, self).__init__()

    def login_page_shutdown_button_click(self):
        """
        点击登录界面关机按钮
        :return:
        """
        self.login_page_shutdown_button().Click()

    def login_page_username_edit_click(self):
        """
        点击用户名编辑框
        :return:
        """
        self.login_page_username_edit().Click()
        if self.login_page_username_edit().GetTextPattern().DocumentRange.GetText() != '':
            self.login_page_username_edit().SendKeys('{Ctrl}a')
            self.login_page_username_edit().SendKeys('{Delete}')

    def login_page_username_edit_sendkeys(self, username):
        """
        登录界面-用户名输入框输入内容
        :param username:用户名
        :return:
        """
        self.login_page_username_edit().SendKeys(username)

    def login_page_password_edit_click(self):
        """
        点击密码编辑框
        :return:
        """
        self.login_page_password_edit().Click()
        if self.login_page_password_edit().GetTextPattern().DocumentRange.GetText() != '':
            self.login_page_password_edit().SendKeys('{Ctrl}a')
            self.login_page_password_edit().SendKeys('{Delete}')

    def login_page_password_edit_sendkeys(self, password):
        """
        登录界面-密码输入框输入内容
        :param password:密码
        :return:
        """
        self.login_page_password_edit().SendKeys(password)

    def login_page_admin_button_click(self):
        """
        点击登录界面【管理员】按钮
        :return:
        """
        self.login_page_admin_button().Click()

    def login_page_user_button_click(self):
        """
        点击登录界面【普通用户】按钮
        :return:
        """
        self.login_page_user_button().Click()

    def login_page_service_button_click(self):
        """
        点击登录界面【技服】按钮
        :return:
        """
        self.login_page_service_button().Click()

    def login_page_login_button_click(self):
        """
        点击登录界面【登录】按钮
        :return:
        """
        self.login_page_login_button().Click()

    def login_page_quit_button_click(self):
        """
        点击登录界面【退出】按钮
        :return:
        """
        self.login_page_quit_button().Click()


if __name__ == '__main__':
    login = LoginPageAction()
    time.sleep(2)
    # login.login_page_admin_button_click()
    # # login.login_page_admin_button_click()
    # login.login_page_password_edit_click()
    # main_window = auto.WindowControl(Name="My3DApp")
    # main_window.EditControl(foundIndex=1).Click()
    my3d = auto.WindowControl(Name="My ThreeD Application", Depth=1)
    my3d.CheckBoxControl(searchDepth=3, foundIndex=8).Click()