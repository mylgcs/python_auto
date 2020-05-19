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

# 1. 显示静态球
y = 100
r = 50
pygame.draw.circle(window, (255, 0, 0), (100, y), r)

# 图片
ix, iy = 50, 200   # 图片坐标
d = 0  # 旋转角度
image = pygame.image.load('files/宝儿姐.jpg')
iw, ih = image.get_size()
window.blit(image, (ix, iy))

pygame.display.update()

# 游戏循环
num = 1
while True:
    num += 1
    # 1) 移动动画
    # if num % 10 == 0:
    #     pygame.draw.circle(window, (255, 255, 255), (100, y), 50)
    #     window.blit(image, (ix, iy))
    #     y = y + 4   # y += 1
    #     pygame.draw.circle(window, (255, 0, 0), (100, y), 50)
    #     pygame.display.update()

    # 2) 缩放动画
    # if num % 10 == 0:
    #     pygame.draw.circle(window, (255, 255, 255), (100, y), r)
    #     r += 1
    #     pygame.draw.circle(window, (255, 0, 0), (100, y), r)
    #     pygame.display.update()

    # 3) 旋转动画
    # if num % 10 == 0:
    #     window.fill((255, 255, 255))
    #     pygame.draw.circle(window, (255, 0, 0), (100, y), r)
    #     # pygame.draw.rect(window, (255, 255, 255), (ix, iy, iw, ih))
    #     d += 1
    #     new_image = pygame.transform.rotozoom(image, d, 1)
    #     window.blit(new_image, (ix, iy))
    #     pygame.display.update()

    # 4）移动和缩放
    if num % 10 == 0:
        pygame.draw.circle(window, (255, 255, 255), (100, y), r)
        window.blit(image, (ix, iy))
        y += 4
        r += 1
        pygame.draw.circle(window, (255, 0, 0), (100, y), r)
        pygame.display.update()

    # 检测事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出
            exit()
