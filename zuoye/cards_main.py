#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from cards_managing import cards_tools
from zuoye import cards_tools
while True :
    #  显示菜单部分
    cards_tools.menu_show()
    function_choose = input("请选择操作功能：")


    if function_choose in ['0', '1', '2', '3'] :
        if function_choose == '1' :
            #新建名片（输入并存储）
            print('您选择的功能是：【1】新建名片')
            print('请输入以下信息：')
            cards_tools.cards_build()
            print('名片添加成功！')
        elif function_choose == '2' :
            # 显示全部
            print('您选择的功能是：【2】显示全部')
            cards_tools.cards_show()
        elif function_choose == '3' :
            #查询名片并操作
            print('您选择的功能是：【3】查询名片')
            cards_tools.cards_find()
        elif function_choose == '0' :
            #退出系统
            print('成功退出系统，欢迎下次使用！')
            break