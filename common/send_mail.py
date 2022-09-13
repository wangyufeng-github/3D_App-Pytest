# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2022/8/9 16:08
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : send_mail.py
# @Software : PyCharm


import time
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import email
import os
from common.log import logger


def send_main(file_path, mail_to='yufeng.wang@we-med.com'):
    mail_from = 'xiaomimang@163.com'
    f = open(file_path, 'rb')
    mail_body = f.read()
    f.close()

    logger.info("开始发送测试报告")
    # msg = email.MIMEMultipart.MIMEMultipart()
    msg = MIMEMultipart()

    # 构造MIMEBase对象做为文件附件内容并附加到根容器
    contype = 'application/octet-stream'
    maintype, subtype = contype.split('/', 1)

    # 读入文件内容并格式化
    data = open(file_path, 'rb')
    # file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
    file_msg = MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()

    # email.Encoders.encode_base64(file_msg)
    encoders.encode_base64(file_msg)

    # 设置附件头
    basename = os.path.basename(file_path)
    file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
    msg.attach(file_msg)
    print(u'msg 附件添加成功')
    logger.info("报告附件添加成功")

    msg1 = MIMEText(mail_body, "html", 'utf-8')
    msg.attach(msg1)

    if isinstance(mail_to, str):
        msg['To'] = mail_to
    else:
        msg['To'] = ','.join(mail_to)
    msg['From'] = mail_from
    msg['Subject'] = u'医学图像处理软件自动化测试'
    msg['date'] = time.strftime('%Y-%m-%d-%H_%M_%S')
    # print(msg['date'])

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('xiaomimang@163.com', 'WFENGENGEAEAQXAP')  # 登录账号和密码（密码为之前申请的授权码）
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    # print(msg['date']+'：测试报告已通过邮件发送!')
    logger.info("测试报告发送成功")

# if __name__=='__main__':
#     sendmain('../report/2017-08-18-10_18_57_result.html')
