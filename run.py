#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob
from behave.__main__ import main as behave_main
import datetime
import os
import shutil
from pathlib import Path

if __name__ == "__main__":
    #遍历删除log文件
    path = Path.cwd().parent
    for name in path.rglob('@AutomationLog.txt'):
        os.remove(name)
    # 设置执行命令和保存路径
    feature_path = os.path.dirname(os.path.realpath(__file__)) + "/features"
    os.chdir(feature_path)
    result_folder = os.path.dirname(os.path.realpath(__file__)) + "/reports/"+datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    allure_dir = result_folder + "/allure-results/"
    run_cmd = ["-f allure_behave.formatter:AllureFormatter", "-o" + allure_dir]
    # 定位feature文件
    ff = glob.glob(feature_path + '/feature/{feature_name}.feature'.format(feature_name="login"))
    run_cmd.extend(ff)
    # 通过Behave源码接执行脚本并将结果保存为json文件到allure-results目录下
    behave_main(run_cmd)
    # 将json结果转换为html
    os.system("allure generate --report-dir {folder}/html-report/ {result} ".format(folder=result_folder,
                                                                       result=allure_dir))
    # # 递归删除生成结果目录
    shutil.rmtree(allure_dir)