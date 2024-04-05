#!/usr/bin/env python
# coding=utf-8
# ------------------------------------------------------------------
# File Name:        main.py
# Author:           dqfzj@foxmail.com
# Created:          2024/4/5 9:53
# Description:
# ------------------------------------------------------------------
import os
import sys
from flask import Flask, render_template

from utils.FileOperate import get_conf

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from webService.Handle import Handle

app = Flask(__name__)


@app.route('/wechat/gpt', methods=['GET'])
def get_handle():
    handle = Handle()
    return handle.get_handle()


@app.route('/wechat/gpt', methods=['POST'])
def wechat_reply():
    handle = Handle()
    return handle.post()


@app.route('/wechat/console_test', methods=['GET'])
def test_console():
    return render_template("index.html")


if __name__ == '__main__':
    debug = get_conf("system", "debug") == "1"
    app.run(host='127.0.0.1', port=9000, debug=debug)
