#!/usr/bin/env python
# coding=utf-8
# ------------------------------------------------------------------
# File Name:        Handle.py
# Author:           dqfzj@foxmail.com
# Created:          2024/4/5 9:53
# Description:
# ------------------------------------------------------------------
import hashlib
import time

from flask import request

from utils.Logger import Logger
from utils.Constant import *
from webService import receive
from webService.ChatGPT import ChatGpt
from webService.HistoryCache import HistoryCache
from webService.Msg import Msg

Q_AND_A = {}
LAST_QUESTION = {}
USER_HISTORY_CACHE = {}


def get_history_by_user(user):
    his = USER_HISTORY_CACHE.get(user)
    new_hist = his
    if his:
        for h in his:
            if not h.tran2msg():
                new_hist.remove(h)
    return new_hist if new_hist else []


def add_history(user, content, msg_type):
    USER_HISTORY_CACHE.update(
        {user: get_history_by_user(user).append(HistoryCache(content, msg_type))}
    )


class Handle:
    def __init__(self):
        self.logger = Logger().get_logger()
        self.req_msg = None

    def get_handle(self):
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

    # @timeout(4)
    def post(self):
        try:
            req_data = request.data

            gpt = ChatGpt()
            self.logger.info(f"get request data is:{str(req_data)}")

            self.req_msg = receive.parse_xml(req_data)
            self.logger.info(f"get request, msg type is {type(self.req_msg)}")

            if isinstance(self.req_msg, Msg) and self.req_msg.MsgType == 'text':
                toUser = self.req_msg.FromUserName
                fromUser = self.req_msg.ToUserName
                input_msg = self.req_msg.input_content.decode('UTF-8', 'strict')
                self.logger.info(f"get request, msg is {input_msg}")
                LAST_QUESTION.update({self.req_msg.FromUserName: input_msg})
                content = Q_AND_A.get(input_msg, None)
                if input_msg == "/clear":
                    content = "clear cache now."
                    self.logger.info(content)
                    return self.req_msg.send(content)
                if input_msg == "1":
                    content = Q_AND_A.get(LAST_QUESTION.get("self.req_msg.FromUserName"), None)
                if not content:
                    import pdb;pdb.set_trace()
                    add_history(self.req_msg.FromUserName, input_msg, INPUT_CONTENT)
                    content = gpt.ask(get_history_by_user(self.req_msg.FromUserName))
                    Q_AND_A.update({input_msg: content})
                    add_history(self.req_msg.FromUserName, content, REPLY_CONTENT)

                self.logger.info(f"get request, ready to send content:{content}")
                return self.req_msg.send(content)
            else:
                self.logger.warning("todo")
                return "success"
        except TimeoutError as timeout:
            self.logger.warning(f"handle failed because timeout")
            content = "网络有点慢哦，请在五秒后输入“1”获取前一个问题的答案。"
            return self.req_msg.send(content)
        except Exception as e:
            self.logger.error(f"handle failed with exception:{str(e)}")
            return str(e)
