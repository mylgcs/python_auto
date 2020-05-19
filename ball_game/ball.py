import pygame
from ball_game.tool import Color
from enum import Enum


class Direction(Enum):
    """方向枚举类"""
    Up = 273
    Left = 276
    Down = 274
    Right = 275


class Ball:
    """球类"""
    window = None

    def __init__(self):
        # 球的图片
        self.image = pygame.image.load('files/ball.png')
        # 球的速度(分两个方向)
        self.x_speed = 4
        self.y_speed = 0
        # 球的大小
        self.width, self.height = self.image.get_size()
        # 球的位置
        win_w, win_h = Ball.window.get_size()
        self.x = win_w/2 - self.width/2
        self.y = win_h/2 - self.height/2
        # 球的方向
        self._direction = Direction.Right

        # 创建球就把球渲染到窗口上
        Ball.window.blit(self.image, (self.x, self.y))
        pygame.display.update()

    def move(self):
        """球移动"""
        self.x += self.x_speed
        self.y += self.y_speed
        Ball.window.fill(Color.WHITE)
        Ball.window.blit(self.image, (self.x, self.y))
        pygame.display.update()

    # 给方向添加getter和setter
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, key):
        """保证在重新给方向赋值的时候就修改球移动的速度"""
        # 上下方向不能直接切换，左右方向不能直接切换
        if self._direction == Direction.Up:
            if key == Direction.Down.value:
                return
        if self._direction == Direction.Down:
            if key == Direction.Up.value:
                return
        if self._direction == Direction.Left:
            if key == Direction.Right.value:
                return
        if self._direction == Direction.Right:
            if key == Direction.Left.value:
                return

        # 修改方向，并且根据方向修改对应的速度
        if key == Direction.Up.value:
            # 上
            print('上')
            self.y_speed = -4
            self.x_speed = 0
            self._direction = Direction.Up
        elif key == Direction.Down.value:
            self.y_speed = 4
            self.x_speed = 0
            self._direction = Direction.Down
        elif key == Direction.Left.value:
            self.y_speed = 0
            self.x_speed = -4
            self._direction = Direction.Left
        elif key == Direction.Right.value:
            self.y_speed = 0
            self.x_speed = 4
            self._direction = Direction.Right
