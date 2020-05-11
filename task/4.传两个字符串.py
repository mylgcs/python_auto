# 写一个函数，传入两个字符串，返回从第一个字符串中去掉第二个字符串中的字符之后的字符串。

def remove_chars(str1,str2):
    str3 = ''
    for ch in str1:
        if ch not in str2:
            str3 += ch
        return str3


print(remove_chars(str1="mayanliang",str2="y"))