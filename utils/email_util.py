# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class EmailUtil:
    def __init__(self):
        self.sender = "1589369708@qq.com"
        self.receivers = "qing.li@moji.com, 13263106808@163.com"
        self.smtpserver = "smtp.qq.com"
        self.username = "1589369708@qq.com"
        self.password = "fbgsrzbjtxlgffag"
        self.mailtitle = "web ui 自动化邮件"

    def send_email(self, path):
        with open(path, 'rb') as f:
            mail_file = f.read()
        message = MIMEText(mail_file, 'html', 'utf-8')
        message['From'] = self.sender
        message['To'] = self.receivers
        message['Subject'] = Header(self.mailtitle, 'utf-8')

        try:
            smtp = smtplib.SMTP_SSL(self.smtpserver, 465)
            smtp.login(self.username, self.password)
            smtp.sendmail(self.sender, self.receivers.split(","), message.as_string())
            smtp.quit()
        except smtplib.SMTPException as e:
            # 改成丁丁报警
            print("邮件发送失败", path, e)
