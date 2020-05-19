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

# 1. 静态球
x, y = 200, 30
r = 30
y_speed = 2
pygame.draw.circle(window, (0, 255, 0), (x, y), r)
pygame.display.update()

num = 0
while True:
    num += 1
    # 小球上下反弹的效果
    if num % 10 == 0:
        window.fill((255, 255, 255))
        # 修改y坐标
        y += y_speed

        # 检测边界
        if y >= WIN_HEIGHT - r:
            y_speed = y_speed * -1

        if y <= r:
            y_speed = y_speed * -1

        pygame.draw.circle(window, (0, 255, 0), (x, y), r)
        pygame.display.update()

    # 检测事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出
            exit()

