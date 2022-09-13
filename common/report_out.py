# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2022/8/9 15:59
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : report_out.py
# @Software : PyCharm
import time
import unittest
from BeautifulReport import BeautifulReport as bf


def report_out(test_dir,report_dir,name_project):
    """
    测试报告模块
    :param test_dir:
    :param report_dir:
    :param name_project:
    :return:
    """
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    report_name = now + '-' + name_project + '_test_report.html'
    run = bf(discover)
    run.report(filename=report_name,report_dir=report_dir,description=U"酷狗音乐UI自动化功能回归测试")
