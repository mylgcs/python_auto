""" 
    @Time : 2020/5/19 16:08 @Author : 马炎亮
    @File : example01.py @Software: PyCharm
    打开文件 ---> open(文件路径, 操作模式, 字符编码)
    读文件 ---> open(文件路径, 'r', encoding=字符编码) ---> file object
    字符集和字符编码问题可以阅读下面的链接：
    https://www.cnblogs.com/skynet/archive/2011/05/03/2035105.html
    read() ---> 读文件 / write() ---> 写文件 / close() ---> 关闭文件
    try ---> 把可能会出状况的代码保护起来执行
    except ---> 捕获异常状况并进行相应的处理
    finally ---> 总是执行代码（不管正常异常其中的代码总是会执行）
    with上下文语法 ---> with open(...) as file ---> 自动释放资源
"""
class InputError(ValueError):
    """自定义异常类型"""
    pass


def fac(num):
    if type(num) != int or num < 0:
        # 使用raise抛出异常对象（引发异常）
        raise InputError('只能计算非负整数的阶乘！！！')
    if num in (0, 1):
        return 1
    return num * fac(num - 1)


def main():
    flag = True
    while flag:
        num = int(input('n = '))
        try:
            print(f'{num}! = {fac(num)}')
            flag = False
        except InputError as err:
            # 打印异常对象（显示异常相关信息）
            print(err)
    try:
        with open('./files/致橡树.txt', mode='r', encoding='utf-8') as file:
            data = file.read(64)
            while data:
                print(data, end='')
                data = file.read(64)
    except FileNotFoundError:
        print('文件不存在，请指定正确的文件路径!!!')
    except LookupError:
        print('指定了无效的编码!!!')
    except UnicodeDecodeError:
        print('指定的编码方式无法解码文件内容!!!')


if __name__ == '__main__':
    main()
