# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import logging
from settings import BASE_DIR


class Logger:
    def __init__(self, path=None):
        if path:
            self.path = path
        else:
            self.path = BASE_DIR + '/log/logs/selenium.log'
        self.logger = logging.getLogger()
        fh = logging.FileHandler(self.path, 'a+', encoding='utf-8')
        sh = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(lineno)s -%(levelname)s -%(message)s")
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addFilter(sh)
        self.logger.setLevel(logging.INFO)
        fh.close()
        sh.close()

    def get_logger(self):
        return self.logger

