# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from page.basePage import BasePage


class BaiduIndexPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(self.driver)

    # 获取输入框
    def input_element(self):
        return self.base_page.element_id("kw")

    # 获取搜索按钮
    def search_button(self):
        # return self.base_page.element_partial_link_text("百度一下")
        return self.base_page.element_xpath("//*[@id='su']")

