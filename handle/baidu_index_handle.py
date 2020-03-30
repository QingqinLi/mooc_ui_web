# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from page.baidu_index_page import BaiduIndexPage


class BaiduIndexHandle:
    def __init__(self, driver):
        self.driver = driver
        self.mooc_index_page = BaiduIndexPage(self.driver)

    # 输入框输入关键字
    def search_set_word(self, word):
        self.mooc_index_page.input_element().send_keys(word)

    # 点击搜索按钮
    def click_search_button(self):
        self.mooc_index_page.search_button().click()