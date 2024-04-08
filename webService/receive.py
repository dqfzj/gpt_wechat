#!/usr/bin/env python
# coding=utf-8
# ------------------------------------------------------------------
# File Name:        receive.py.py
# Author:           dqfzj@foxmail.com
# Created:          2024/4/5 23:21
# Description:      
# ------------------------------------------------------------------

import json
import xml.etree.ElementTree as ET

from webService.Msg import TextMsg, ImageMsg


def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xml_data = ET.fromstring(web_data)
    msg_type = xml_data.find('MsgType').text
    if msg_type == 'text':
        return TextMsg(xml_data)
    elif msg_type == 'image':
        return ImageMsg(xml_data)


def parse_json(web_data):
    """解析json"""
    if len(web_data) == 0:
        return None
    data = json.loads(web_data)
    msg_type = data.get('MsgType')
    if msg_type == 'text':
        return TextMsg(data)
    elif msg_type == 'image':
        return ImageMsg(data)
