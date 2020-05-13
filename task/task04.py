# 写一个装饰器，实现将被装饰函数返回的字符串每个单词首字母大写的功能。
from functools import wraps

def render_to_title(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == str:
            result = result.title()
        return result

    return wrapper



print(render_to_title('mayanliang'))
