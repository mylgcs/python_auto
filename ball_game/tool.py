from random import randint


class Color:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    @staticmethod
    def random_color():
        """随机颜色"""
        return randint(0, 255), randint(0, 255), randint(0, 255)
