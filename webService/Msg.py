#!/usr/bin/env python
# coding=utf-8
# ------------------------------------------------------------------
# File Name:        Msg.py
# Author:           dqfzj@foxmail.com
# Created:          2024/4/5 23:24
# Description:      
# ------------------------------------------------------------------
import time


class Msg(object):
    def __init__(self, xml_data):
        self.ToUserName = xml_data.find('ToUserName').text
        self.FromUserName = xml_data.find('FromUserName').text
        self.CreateTime = xml_data.find('CreateTime').text
        self.MsgType = xml_data.find('MsgType').text
        self.MsgId = xml_data.find('MsgId').text

    def send(self, content=None):
        return "success"


class TextMsg(Msg):
    def __init__(self, xml_data):
        Msg.__init__(self, xml_data)
        self.input_content = xml_data.find('Content').text.encode("utf-8")

    def send(self, content=None):
        xml_form = f"""
            <xml>
                <ToUserName><![CDATA[{self.FromUserName}]]></ToUserName>
                <FromUserName><![CDATA[{self.ToUserName}]]></FromUserName>
                <CreateTime>{int(time.time())}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{content}]]></Content>
            </xml>
            """
        return xml_form


class ImageMsg(Msg):
    def __init__(self, xml_data):
        Msg.__init__(self, xml_data)
        self.PicUrl = xml_data.find('PicUrl').text
        self.MediaId = xml_data.find('MediaId').text

    def send(self, content=None):
        xml_form = f"""
            <xml>
                <ToUserName><![CDATA[{self.FromUserName}]]></ToUserName>
                <FromUserName><![CDATA[{self.ToUserName}]]></FromUserName>
                <CreateTime>{int(time.time())}</CreateTime>
                <MsgType><![CDATA[image]]></MsgType>
                <Image>
                <MediaId><![CDATA[{self.MediaId}]]></MediaId>
                </Image>
            </xml>
            """
        return xml_form
