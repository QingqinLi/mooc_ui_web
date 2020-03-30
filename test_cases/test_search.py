# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from bussiness.baidu_search_business import BaiduSearchBusiness
import pytest
from page.basePage import BasePage


class TestSearch:

    @pytest.mark.parametrize(
        "keyword",
        [
            "中文",
            "test",
            " ",
        ],
        ids=["test_chinese", "test_english", "test_space"]
    )
    def test_search_keyword(self, get_browser,keyword):
        get_browser.get("https://www.baidu.com")
        assert BaiduSearchBusiness(get_browser).search_keyword(keyword)
