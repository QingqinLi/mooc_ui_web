# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import pytest
import time
from settings import BASE_DIR
from utils.command import Command
from utils.email_util import EmailUtil
from utils.alert import Alert
from log.log import Logger


class RunTest:
    def __init__(self):
        self.cmd = Command()
        self.email_util = EmailUtil()
        self.alert = Alert()
        self.logger = Logger().get_logger()

    def main(self):
        time_stamp = str(int(time.time()))
        file_path = BASE_DIR + '/report/html_report/'+time_stamp+".html"
        test_dir = BASE_DIR + '/test_cases'
        allure_reports = BASE_DIR + '/report/allure_reports'
        allure_report = BASE_DIR + '/report/allure_report'
        pytest.main([test_dir,
                     '-v',
                     '-s',
                     '--html='+file_path,
                     '--alluredir='+allure_reports,
                     '--reruns', '2',
                     '--reruns-delay', '2'])
        # 本地生成allure报告，jenkins配置allure， 不需要执行命令
        # cmd = "allure generate "+allure_reports+" -o "+allure_report + " --clean"
        # result = self.cmd.execute_result_cmd(cmd)
        self.email_util.send_email(file_path)
        self.alert.send_text("ui测试完成, 已发送邮件")
        self.logger.info("ui测试完成，邮件已发送")


if __name__ == '__main__':
    runner = RunTest()
    runner.main()