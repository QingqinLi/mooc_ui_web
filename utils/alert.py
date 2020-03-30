# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import requests

WEB_HOOK = 'https://oapi.dingtalk.com/robot/send?access_token=382989c022d5fe882e9c6aa12e1f357b97176b4f4b429d32122dd7b888e5f5a4'


class Alert:
    def __init__(self):
        self.web_hook = WEB_HOOK
        self.headers = {
            'Content-Type': 'application/json; charset=utf-8',
        }

    def send_text(self, msg):
        """
        钉钉告警，发送text消息
        :param msg:
        :return:
        """
        data = {'msgtype': "text"}
        if self._is_text_null(msg):
            data['text'] = {'content': msg}
        else:
            raise ValueError("消息不能为空")
        self._ding_post(data)

    def _is_text_null(self, msg):
        if not msg:
            return False
        else:
            return True

    def _ding_post(self, data):
        """
        发送消息（内容UTF-8编码）
        :param data: 消息数据（字典）
        """
        try:
            response = requests.post(self.web_hook, headers=self.headers, json=data)

        except requests.exceptions.HTTPError as exc:
            print("报警消息发送失败， HTTP error: %d, reason: %s" % (exc.response.status_code, exc.response.reason))

        except requests.exceptions.ConnectionError:
            print("报警消息发送失败，HTTP connection error!")

        else:
            send_result = response.json()
            if send_result['errcode']:
                print("钉钉机器人消息发送失败，原因：%s" % send_result['errmsg'])

