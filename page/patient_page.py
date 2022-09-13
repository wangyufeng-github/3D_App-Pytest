# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2022/8/12 9:53
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : patient_page.py
# @Software : PyCharm
import uiautomation


class PatientPage:
    def __init__(self):
        self.patient_window = uiautomation.WindowControl(Name="My ThreeD Application")

    def patient_window_top_title_bar_week(self):
        """
        病人数据管理界面-week按钮
        :return:
        """
        return self.patient_window.RadioButtonControl(Name="Week")

    def patient_window_top_title_bar_month(self):
        """
        病人数据管理界面-month按钮
        :return:
        """
        return self.patient_window.RadioButtonControl(Name="Month")

    def patient_window_top_title_bar_all(self):
        """
        病人数据管理界面-all按钮
        :return:
        """
        return self.patient_window.RadioButtonControl(Name="All")

    def patient_window_top_title_bar_name_edit(self):
        """
        病例管理界面-上方标题栏【用户名】输入框
        :return:
        """
        return self.patient_window.TextControl(Name="姓名").GetNextSiblingControl()

if __name__ == '__main__':
    # print(uiautomation.GetCursorPos())  #获取当前鼠标位置

    res = PatientPage().patient_window_top_title_bar_name_edit()
    print(res)