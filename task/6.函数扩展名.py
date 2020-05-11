# 写一个函数，返回给定文件名的后缀名（扩展名）。

def get_suffix(filename):
    pos = filename.rfind('.')
    return filename[pos + 1:] if pos > 0 else ""

print(get_suffix("mayan.html"))