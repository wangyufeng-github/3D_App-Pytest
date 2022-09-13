# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2022/8/5 16:20
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : tool.py
# @Software : PyCharm
import time
import os
import shutil
import glob
import configparser
from pathlib import Path
from common.log import logger
# 配置文件路径
CONFIG_FILE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\config\config.ini'


class Tool:
    def __init__(self):
        pass

    def get_process_state(self, process_name):
        """
        判断程序是否运行
        :param process_name:
        :return:
        """
        result = os.system(f"tasklist | findstr {process_name}")
        if result is not None:
            return True
        else:
            return False

    def get_config(self, section, option):
        """
        读取配置文件中的用户名和密码信息
        :param section:
        :param value:
        :return:
        """
        config = configparser.ConfigParser()
        filename = CONFIG_FILE_DIR
        print(filename)
        config.read(filename, encoding='utf-8')
        result = config.get(section, option)
        return result

    def delete_html_files(self, file_path):
        """
        清空文件夹
        :param file_path:html文件路径，不包含具体文件名
        :return:
        """
        try:
            for file in os.listdir(file_path):
                if file.endswith('html'):
                    full_path = (os.path.join(file_path, file))
                    full_path = '/'.join(full_path.split('\\'))
                    os.remove(full_path)
                    logger.info("reports文件夹删除html文件成功！")
        except PermissionError as e:
            print("reports文件夹暂时未生成html文件")

    def delete_automationlog_txt(self):
        """
        遍历工程路径的方式删除所有的@AutomationLog.txt文件
        :return:
        """
        path = Path.cwd().parent
        for name in path.rglob('@AutomationLog.txt'):
            os.remove(name)

    def stop_application(self):
        """
        强制退出软件
        :return:
        """
        os.system("taskkill /im My3DApp.exe -f")
        time.sleep(2)


if __name__ == '__main__':
    # Tool().delete_automationlog_txt()
    path = Path.cwd().parent
    for i1 in path.rglob('@AutomationLog.txt'):
        os.remove(i1)
