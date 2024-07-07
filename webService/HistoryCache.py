#!/usr/bin/env python
# coding=utf-8
# ------------------------------------------------------------------
# File Name:        HistoryCache.py
# Author:           dqfzj@foxmail.com
# Created:          2024/7/7 9:53
# Description:
# ------------------------------------------------------------------
import datetime

from utils.Constant import *


class HistoryCache():
    def __init__(self, content, msg_type):
        self.content = content
        self.type = msg_type
        self.time = datetime.datetime.utcnow()

    def get_role(self):
        return "user" if self.type == INPUT_CONTENT else "assistant"

    def tran2msg(self):
        if datetime.timedelta(minutes=15) + self.time < datetime.datetime.utcnow():
            return {}

        return {"role": self.get_role(), "content": self.content}
