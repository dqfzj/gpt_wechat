#!/usr/bin/env bash
path=/var/log/gpt_wechat/

process=`ps aux | grep main.py | grep -v grep`;
if [[ "$process" == "" ]]
then
    python3 /opt/wechat/gongzhonghao/gpt_wechat/main.py
fi
