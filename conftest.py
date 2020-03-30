# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import pytest
from selenium import webdriver
import allure


browser = 'Chrome'
driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中\
    :param item:
    """
    print("item", item)

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    report.description = str(item.function.__doc__)

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # file_name = report.nodeid.replace("::", "_")+".png"
            # screen_img = _capture_screenshot_base64()
            # if file_name:
            #     html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:300px;height:600px;" ' \
            #            'onclick="window.open(this.src)" align="right"/></div>' % screen_img
            #     extra.append(pytest_html.extras.html(html))
            # print("到这里了吗")
            with allure.step('添加失败截图...'):
                print("yahahah")
                allure.attach(_capture_screenshot(), "失败截图", allure.attachment_type.PNG)
            print("allure截图了吗")
        report.extra = extra


def _capture_screenshot():
    return driver.get_screenshot_as_png()


@pytest.fixture(scope='session', autouse=True)
def get_browser():
    global driver
    if not driver:
        if browser == 'Chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
    yield driver
    driver.quit()
    return driver

