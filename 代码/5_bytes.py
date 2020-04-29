#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: 5_bytes.py
@time: 2020/4/26 9:53 上午
'''
b1 = b'hello'  # 只能是ascii码
print(type(b1))
# python字符串转bytes
# b2 = "好".encode("utf8")
# print(b2,type(b2))
# bytes=>python字符串
# b3 = b1.decode('utf8')
# print(b3,type(b3))

# 签名
import hashlib
password= '124'
password = hashlib.sha1(password.encode('utf8')).hexdigest()
print(password)
