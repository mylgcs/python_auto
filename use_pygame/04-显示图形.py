import pygame
from math import pi

pygame.init()
window = pygame.display.set_mode((400, 600))
pygame.display.set_caption('显示图形')
# 设置背景颜色
window.fill((255, 255, 255))

# ===============显示图形===============
# 1. 画直线
# line(画在哪儿, 线的颜色, 线的起点, 线的终点, 线宽=1)
pygame.draw.line(window, (255, 0, 0), (10, 20), (200, 20))

# 2. 画折线
# lines(画在哪儿, 线的颜色, 是否闭合, 多个点, 线宽=1)
points = [(10, 300), (100, 160), (180, 260), (300, 100)]
pygame.draw.lines(window, (0, 255, 0), True, points, 3)

# 3. 画圆
# circle(画在哪儿, 线的颜色, 圆心坐标, 半径, 线宽=0)
pygame.draw.circle(window, (0, 0, 255), (200, 250), 100, 2)

# 4. 画矩形
# rect(画在哪儿, 线的颜色, 矩形范围, 线宽=0)
pygame.draw.rect(window, (120, 20, 60), (30, 70, 100, 200), 3)

# 5. 画椭圆
# ellipse(画在哪儿, 线的颜色, 矩形范围, 线宽=0)
pygame.draw.ellipse(window, (255, 0, 0), (30, 70, 100, 200), 3)

# 6. 画弧线
# arc(画在哪儿, 线的颜色, 矩形范围, 起始弧度, 终止的弧度, 线宽=1)
pygame.draw.arc(window, (0, 0, 0), (30, 70, 100, 200), 0, pi, 4)


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
