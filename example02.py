""" 
    @Time : 2020/5/19 19:21 @Author : 马炎亮
    @File : example02.py @Software: PyCharm
    写文件
    截断原来的内容写入 ---> open(文件路径, 'w', encoding=字符编码) ---> file object
    在原来的内容后追加 ---> open(文件路径, 'a', encoding=字符编码) ---> file object
"""
def main():
    try:
        with open('files/静夜思.txt', mode='w', encoding='gbk') as file:
            file.write('床前明月光\n')
            file.write('疑似地上霜\n')
            file.write('举头望明月\n')
            file.write('低头思故乡\n')
    except LookupError:
        print('指定了无效的编码')
    except:
        print('代码出问题了，请联系客服人员!!!')


if __name__ == '__main__':
    main()
