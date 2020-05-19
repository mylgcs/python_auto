from random import randint


class Color:
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)

    @staticmethod
    def randow_color():
        return randint(0, 255), randint(0, 255), randint(0, 255)

    @staticmethod
    def rgb(r, g, b):
        return r, g, b
