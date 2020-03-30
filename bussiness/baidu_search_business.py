# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from handle.baidu_index_handle import BaiduIndexHandle
from handle.baidu_result_handle import BaiduResultHandle
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By


class BaiduSearchBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.baidu_index_handle = BaiduIndexHandle(self.driver)
        self.baidu_result_handle = BaiduResultHandle(self.driver)

    def search_keyword(self, word):
        self.baidu_index_handle.search_set_word(word)
        self.baidu_index_handle.click_search_button()
        time.sleep(3)
        # WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located())
        # WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'result')))
        # WebDriverWait(self.driver, 10, 0.5).until(EC.title_contains("结果"))
        print("title", self.driver.title)
        if word in self.driver.title:
            return True
        else:
            return False