import os
import time


# 1. 定义类
class Clock:
    """时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def show(self):
        """报时"""
        print(f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}')

    def run(self):
        """走字"""
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0


def main():
    # 2. 创建对象
    clock = Clock(23, 59, 58)
    while True:
        # os.system('clear')
        # 3. 给对象发消息
        clock.show()
        # 休眠1秒钟
        time.sleep(1)
        # 4. 给对象发消息
        clock.run()


if __name__ == '__main__':
    main()
