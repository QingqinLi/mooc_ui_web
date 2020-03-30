# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
# 执行系统命令

import os
import subprocess
from settings import BASE_DIR


class Command:
    def execute_cmd(self, cmd):
        log_file = BASE_DIR + '/log/logs/system_cmd.log'
        subprocess.Popen(cmd, shell=True, stdout=open(log_file, 'a+'), stderr=subprocess.STDOUT)

    def execute_result_cmd(self, cmd):
        result_list = []
        result = os.popen(cmd).readlines()
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list
