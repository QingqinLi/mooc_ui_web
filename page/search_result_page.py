# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from page.basePage import BasePage


class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.basePage = BasePage(self.driver)

    def search_result(self):
        self.driver.find_elements_by_class_name("result")


