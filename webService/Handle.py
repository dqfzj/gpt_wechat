#!/usr/bin/env python
# coding=utf-8
# ------------------------------------------------------------------
# File Name:        Handle.py
# Author:           dqfzj@foxmail.com
# Created:          2024/4/5 9:53
# Description:
# ------------------------------------------------------------------
import hashlib
from flask import request

from utils.Logger import Logger


class Handle:
    def __init__(self):
        self.logger = Logger()

    def execute(self):
        try:
            data = request.args
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.get('signature')
            timestamp = data.get('timestamp')
            nonce = data.get('nonce')
            echostr = data.get('echostr')
            token = "test20240404"  # 请按照公众平台官网\基本配置中信息填写

            list_input = [token, timestamp, nonce]
            list_input.sort()
            sha1 = hashlib.sha1()
            for item in list_input:
                sha1.update(item.encode('utf-8'))
            hashcode = sha1.hexdigest()
            self.logger.info(f"hashcode:{hashcode}, signature:{signature} ")
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as e:
            self.logger.error(f"handle failed with exception:{str(e)}")
            return str(e)
