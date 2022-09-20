import time
from behave import *
from common.image_match import ImageMatch
from common.log import logger
from common.tool import Tool

def before_scenario(scenario,context):
    ImageMatch().image_to_click("app_icon")
    time.sleep(10)
    login_state = Tool().get_process_state("My3DApp")
    if login_state:
        logger.info("软件成功启动")
    else:
        print("未获取到后台进程，请检查程序是否启动")
        logger.info("软件启动失败")

def after_scenario(scenario,context):
    time.sleep(2)
    Tool().stop_application()
    logger.info("软件已退出")