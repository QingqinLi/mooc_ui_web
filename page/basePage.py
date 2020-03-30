# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.open(url)

    def element_id(self, id_name):
        return self.driver.find_element_by_id(id_name)

    def element_class(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    def element_tag(self, tag_name):
        return self.driver.find_element_by_tag_name(tag_name)

    def element_link_text(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def element_partial_link_text(self, link_text):
        return self.driver.find_element_by_partial_link_text(link_text)

    def element_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def element_css(self, css):
        return self.driver.find_element_by_css(css)
