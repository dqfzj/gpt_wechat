#!/usr/bin/env python
# coding=utf-8
# ------------------------------------------------------------------
# File Name:        main.py
# Author:           dqfzj@foxmail.com
# Created:          2024/4/5 9:53
# Description:
# ------------------------------------------------------------------
from flask import Flask


app = Flask(__name__)


@app.route('/wechat')
def index():
    return {
        "msg": "success",
        "data": "welcome."
    }


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
