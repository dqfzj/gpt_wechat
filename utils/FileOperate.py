#!/usr/bin/env python
# coding=utf-8
# ------------------------------------------------------------------
# File Name:        FileOperate.py
# Author:           dqfzj@foxmail.com
# Created:          2024/4/5 9:54
# Description:      
# ------------------------------------------------------------------
import configparser
import platform


def get_os():
    """
    获取系统类型
    """
    return platform.system().lower()


def get_conf(setion, key):
    cf = configparser.ConfigParser()
    cf.read("../conf/server.conf", encoding='utf-8')
    return cf.get(setion, key)

