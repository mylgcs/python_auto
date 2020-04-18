# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:17:33 2019

@author: LuDuo
"""

import itchat
import requests

api_key='b7963126cccb06adb7db1345b3d85836'
api_secret='5jr5urjsw1zt'
def get_response(msg):
    apiurl = 'http://i.itpk.cn/api.php'  #//moli机器人的网址
    data={
        "question": msg,    #//获取到聊天的文本信息
        "api_key": api_key,
        "api_secret":api_secret
    }

    r=requests.post(apiurl,data=data)  #//构造网络请求
    return r.text
@itchat.msg_register(itchat.content.TEXT)     #//好友消息的处理
def print_content(msg):
    return get_response(msg['Text'])
@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)    #//群消息的处理
def print_content(msg):
    return get_response(msg['Text'])
itchat.auto_login(True)           #//自动登录
itchat.run()                       #//启动聊天机器人