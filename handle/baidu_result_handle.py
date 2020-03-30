# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from page.search_result_page import SearchResultPage


class BaiduResultHandle:
    def __init__(self, driver):
        self.driver = driver
        self.search_result_page = SearchResultPage(driver)

    def get_result_len(self):
        self.search_result_page.search_result()

