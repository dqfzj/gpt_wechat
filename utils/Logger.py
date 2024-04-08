#!/usr/bin/env python
# coding=utf-8
# ------------------------------------------------------------------
# File Name:        Logger.py
# Author:           dqfzj@foxmail.com
# Created:          2024/4/5 9:53
# Description:      
# ------------------------------------------------------------------
import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler

from utils.FileOperate import get_conf, get_os


class Logger:
    def __init__(self):
        self.logger = logging.getLogger("wechat")
        self.logger.setLevel(logging.INFO)

        # 1 for debug
        if get_conf("system", "debug") == "1":
            self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d >>> %(message)s")
        log_path = get_conf("log", f"{get_os()}_path") + get_conf("log", "name")
        # if log path is not exist, create first
        if not os.path.exists(os.path.dirname(log_path)):
            os.makedirs(os.path.dirname(log_path))

        # Create handlers for logging to the standard output and a file
        stdout_handler = logging.StreamHandler(stream=sys.stdout)
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(fmt)

        # 每 1(interval) 天(when) 重写1个文件,保留7(backupCount) 个旧文件；when还可以是Y/m/H/M/S
        file_handler = TimedRotatingFileHandler(log_path, encoding="utf-8", when='d', interval=1, backupCount=30)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(fmt)
        if not self.logger.handlers:
            if get_os() == "windows":
                self.logger.addHandler(stdout_handler)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger
