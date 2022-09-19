from behave import *
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
from assertpy import assert_that

@Given("点击管理员按钮")
def step_impl(context):
    LoginPageAction().login_page_admin_button_click()

@When("点击用户名输入框")
def step_impl(context):
    LoginPageAction().login_page_username_edit_click()

@When("输入用户名{username}")
def step_impl(context,username):
    LoginPageAction().login_page_username_edit_sendkeys(username)

@When("点击密码输入框")
def step_impl(context):
    LoginPageAction().login_page_password_edit_click()

@When("输入密码{password}")
def step_impl(context,password):
    LoginPageAction().login_page_password_edit_sendkeys(password)

@When("点击登录按钮")
def step_impl(context):
    LoginPageAction().login_page_login_button_click()
    logger.info("登录界面点击登录按钮，执行登录操作")

@Then("判断病例管理界面是否显示{status_value}")
def step_impl(context,status_value):
    sleep(5)
    patient_window = auto.StatusBarControl(Name="进入病例管理", Depth=2)
    status = OperateWindow().window_exists(patient_window)
    if status:
        logger.info("软件登录成功，进入病人管理界面")
    assert_that(status).is_equal_to(status_value)




