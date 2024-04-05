#!/usr/bin/python3
# coding=utf-8
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return {
        "msg": "success",
        "data": "welcome."
    }


if __name__ == '__main__':
    # app.run(host='112.10.236.251', port=9000, debug=True)
    app.run(host='192.168.16.167', port=9000, debug=True)
