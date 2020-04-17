import requests

url = 'https://graceui.oss-cn-beijing.aliyuncs.com/grace2020banners/index-banner-01.png'
response = requests.get(url).content

print(response)

with open('代码.png', 'wb') as file:
    file.write(response)
