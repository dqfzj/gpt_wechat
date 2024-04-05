#!/usr/bin/env python
# coding=utf-8
# ------------------------------------------------------------------
# File Name:        FileOperate.py
# Author:           dqfzj@foxmail.com
# Created:          2024/4/5 9:54
# Description:      
# ------------------------------------------------------------------
import configparser
import os
import platform


def get_os():
    """
    获取系统类型
    """
    return platform.system().lower()


def get_conf(section, key):
    cf = configparser.ConfigParser()
    conf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../conf/server.conf"))
    cf.read(conf_path, encoding='utf-8')

    return cf.get(section, key)
