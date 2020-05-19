""" 
    @Time : 2020/5/19 19:22 @Author : 马炎亮
    @File : example04.py @Software: PyCharm
    读取网络资源保存到本地文件
    URL - Universal/Uniform Resource Locator - 统一资源定位符
    唯一标识网络上的一个资源
    --> https://www.baidu.com:443/index.html ---> 百度首页
    --> http://www.sohu.com:80/index.html ---> 搜狐首页

    可以使用requests三方库来进行网络连接 ---> 简单好用，中文文档
    requests的中文文档：https://requests.readthedocs.io/zh_CN/latest/

    pip是Python的包管理工具（查询/安装/卸载/更新 三方库或者三方工具）
    pip install requests -i https://pypi.doubanio.com/simple
"""

import requests


# HTTP Request 向服务器发起一个请求
# HTTP Response 服务器会给浏览器一个响应
def main():
    resp = requests.get('https://www.sohu.com/index.html')
    if resp.status_code == 200:
        with open('files/sohu_index.html', 'w', encoding='utf-8') as file:
            file.write(resp.text)
    else:
        print('请求服务器时发生错误!!!')
    resp = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
    with open('files/baidu_logo.png', 'wb') as file:
        file.write(resp.content)


if __name__ == '__main__':
    main()
