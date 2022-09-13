# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2022/9/1 9:39
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : run_all.py
# @Software : PyCharm
import os
import time
from pathlib import Path

import pytest
import shutil
from common.send_mail import send_main
from common.tool import Tool


def acquire_report_address(reports_address):
    """
    返回最新测试报告完整路径
    :param reports_address:
    :return:
    """
    # 展示报告路径下所有文件
    test_reports_list = os.listdir(reports_address)
    # 文件排序
    new_file_list = []
    for file_name in test_reports_list:
        if file_name.endswith('.html'):
            new_file_list.append(file_name)
    new_test_reports_list = sorted(new_file_list)
    # 获取最新报告
    the_last_report = new_test_reports_list[-1]
    the_last_report_address = os.path.join(reports_address, the_last_report)
    return the_last_report_address


def run_case():
    # 遍历删除文件夹下所有的@AutomationLog.txt
    path = Path.cwd().parent
    for name in path.rglob('@AutomationLog.txt'):
        os.remove(name)
    print("======开始执行=======")
    # 获取当前文件路径
    curpath = os.path.dirname(os.path.realpath(__file__))
    report_dir = os.path.join(curpath, "reports/")
    # 清空报告路径
    Tool().delete_html_files(report_dir)
    test_dir = os.path.join(curpath, "testcase/")
    # 默认执行当前路径及子目录下的测试用例文件
    pytest.main(['--report=autotest_report.html',
                 '--title=医学影像处理软件测试报告',
                 '--tester=王玉峰',
                 '--desc=报告描述信息',
                 '--template=2'])
    time.sleep(8)
    send_main(acquire_report_address(report_dir), mail_to=["yufeng.wang@we-med.com"])
    print("=====执行结束=======")


if __name__ == '__main__':
    run_case()
    # print(acquire_report_address("E:\project\\3DApp\\reports"))