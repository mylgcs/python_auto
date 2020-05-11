# 写一个函数，实现对字符串的加密，假设字符串中只有小写英文字母和空格，加密规则是a变d，b变e，c变f，……，x变a，y变b，z变c，空格保持不变。

def encrypt(massage):
    result = ""
    for ch in massage:
        if ch == " ":
            result += ch
        elif 'a' <= ch <= "w":
            result += chr(ord(ch)+3)
        else:
            result += chr(ord(ch)-23)
    return result

print(encrypt("mayan liang"))