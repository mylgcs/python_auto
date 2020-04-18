#!/usr/bin/python
# -*- coding: UTF-8 -*-
info_dic = {}
cards_list = []
def menu_show() :  #菜单显示函数
    print('*' * 50)
    print('欢迎使用【名片管理系统】 V 1.0')
    print('')
    print('【1】新建名片')
    print('【2】显示全部')
    print('【3】查询名片')
    print('')
    print('【0】退出系统')
    print('*' * 50)

def cards_build() :   #名片建立函数
    name_str = input('姓名（name）：')
    university_str = input('大学（university）：')
    grade_str = input('年级（grade）：')
    major_str = input('专业（major）：')
    info_dic = {'姓名（name）：': name_str,
           '大学（university）：': university_str,
           '年级（grade）：': grade_str,
           '专业（major）：': major_str}

    cards_list.append(info_dic)

def cards_show() :   #显示全部名片函数
    for information in ['姓名(name)', '大学(university)', '年级(grade)', '专业(major)'] :
        print(information, end= '\t\t')
    print('')
    print('=' * 65)


    for info_dic in cards_list :
        print('%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s'  %(info_dic['姓名（name）：'],
                                        info_dic['大学（university）：'],
                                        info_dic['年级（grade）：'],
                                        info_dic['专业（major）：']))

def cards_find() :    #名片查询函数
    name_find = input('请输入要查询的名字：')
    for person in cards_list :
        if person['姓名（name）：'] ==name_find :
            print('查询结果为：')
            for information in ['姓名(name)', '大学(university)', '年级(grade)', '专业(major)']:
                print(information, end='\t\t')
            print('')
            print('=' * 65)

            print('%s\t\t%s\t\t%s\t\t%s' %(person['姓名（name）：'],
                                           person['大学（university）：'],
                                           person['年级（grade）：'],
                                           person['专业（major）：']))
            cards_deal(person)
            break
    else:
        print('名片系统查无此人！')

def cards_deal(person_find) :     #处理名片的函数
    deal_choose = input('请输入要执行的操作：\n【1】修改名片\n【2】删除名片\n【3】复制名片\n【4】返回主菜单')
    if deal_choose in ['1', '2' ,'3', '4'] :
        if deal_choose == '1' :
            print('请输入需要重新修改的信息：')
            person_find['姓名（name）：'] = input_new(person_find['姓名（name）：'], '姓名（name）:')
            person_find['大学（university）：'] = input_new(person_find['大学（university）：'], '大学(university) :')
            person_find['年级（grade）：'] = input_new(person_find['年级（grade）：'], '年级(grade) :')
            person_find['专业（major）：'] = input_new(person_find['专业（major）：'], '专业(major) :')
            print('修改名片成功！')

        elif deal_choose == '2' :    #删除名片
            cards_list.remove(person_find)
            print('删除名片成功！')

        elif deal_choose == '3' :     #复制名片
            cards_list.append(person_find)
            print('复制名片成功！')

        elif deal_choose == '4' :    #返回主菜单
            pass

def input_new(info_new, tip_message) :    #定义一个新的输入函数
    info_receive = input(tip_message)
    if len(info_receive) > 0 :  #如果有输入，就返回输入
        return info_receive
    else:                      #如果没有输入，就返回信息的原有值
        return info_new