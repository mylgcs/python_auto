import pygame
from ball_game.tool import Color
from ball_game.ball import Ball

WIDTH, HEIGHT = 800, 600


def game_system():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window.fill(Color.WHITE)
    pygame.display.update()

    Ball.window = window
    player = Ball()

    frame = 0
    while True:
        # 游戏帧的刷新
        if frame % 100 == 0:
            player.move()

        for event in pygame.event.get():
            # 事件处理
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                player.direction = event.key


if __name__ == '__main__':
    game_system()
