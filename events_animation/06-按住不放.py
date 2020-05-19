import pygame

WIN_WIDTH = 400    # 窗口宽度
WIN_HEIGHT = 600   # 窗口高度

# 初始化游戏
pygame.init()

# 创建窗口
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('动画原理')
window.fill((255, 255, 255))
pygame.display.flip()

# 放坦克
tank_up = pygame.image.load('files/p1tankU.gif')   # 向上的坦克
tank_down = pygame.image.load('files/p1tankD.gif')
tank_left = pygame.image.load('files/p1tankL.gif')
tank_right = pygame.image.load('files/p1tankR.gif')
tank = tank_up
tank_x, tank_y = 200, 450

window.blit(tank, (tank_x, tank_y))
pygame.display.update()

is_move = False   # 是否移动
x_speed = 0
y_speed = 0
while True:
    if is_move:
        window.fill((255, 255, 255))
        tank_x += x_speed
        tank_y += y_speed
        window.blit(tank, (tank_x, tank_y))
        pygame.display.update()
    # 检测事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出
            exit()
        if event.type == pygame.KEYDOWN:
            char = chr(event.key)
            # 往上
            if char == 'w':
                is_move = True
                x_speed = 0
                y_speed = -2
                tank = tank_up
            # 向左
            if char == 'a':
                is_move = True
                x_speed = -2
                y_speed = 0
                tank = tank_left
            # 向下
            if char == 's':
                is_move = True
                x_speed = 0
                y_speed = 2
                tank = tank_down
            # 向右
            if char == 'd':
                is_move = True
                x_speed = 2
                y_speed = 0
                tank = tank_right
        if event.type == pygame.KEYUP:
            is_move = False
