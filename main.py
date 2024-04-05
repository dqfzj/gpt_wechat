#!/usr/bin/env python
# coding=utf-8
# ------------------------------------------------------------------
# File Name:        main.py
# Author:           dqfzj@foxmail.com
# Created:          2024/4/5 9:53
# Description:
# ------------------------------------------------------------------
from flask import Flask, render_template

from webService.Handle import Handle

app = Flask(__name__)


@app.route('/wechat', methods=['GET'])
def get_handle():
    handle = Handle()
    return handle.execute()


@app.route('/', methods=['GET'])
@app.route('/test', methods=['GET'])
def test_console():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
