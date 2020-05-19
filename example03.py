""" 
    @Time : 2020/5/19 19:22 @Author : 马炎亮
    @File : example03.py @Software: PyCharm
    读写二进制文件
"""

def main():
    with open('files/guido.jpg', mode='rb') as file1, \
            open('files/龟叔.jpg', mode='wb') as file2:
        data = file1.read(512)
        counter = 0
        while data:
            counter += 1
            file2.write(data)
            data = file1.read(512)


if __name__ == '__main__':
    main()
