import pygame
from random import randint

WIN_WIDTH = 400    # 窗口宽度
WIN_HEIGHT = 600   # 窗口高度

# 初始化游戏
pygame.init()

# 创建窗口
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('动画原理')
window.fill((255, 255, 255))
pygame.display.flip()

# 字体
font = pygame.font.Font('files/t2.ttf', 30)
tx = 0

count = 0   # 统计事件发生的次数
while True:
    # 检测事件
    for event in pygame.event.get():
        # for循环中的代码只有事件发生后才会执行
        count += 1
        print(count)

        # event的type属性是用来区分不同类型的事件
        """
        QUIT   -  点击关闭按钮对应的事件
        
        1. 鼠标事件
        MOUSEBUTTONDOWN  - 鼠标按下
        MOUSEBUTTONUP - 鼠标弹起
        MOUSEMOTION - 鼠标移动
        
        鼠标位置属性(点的哪儿)  - pos
        
        
        2. 键盘事件
        KEYDOWN -  按键被按下
        KEYUP - 按键弹起
        
        按键值属性(哪个键被按了)  - key
        """
        if event.type == pygame.QUIT:
            # 退出
            exit()

        # =================鼠标事件====================
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('鼠标按下', event.pos)
            mx, my = event.pos    # 取出鼠标的x坐标和y坐标
            pygame.draw.circle(window, (255, 255, 0), (mx, my), 50)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONUP:
            print('鼠标弹起')

        if event.type == pygame.MOUSEMOTION:
            # print('鼠标移动')
            mx, my = event.pos  # 取出鼠标的x坐标和y坐标
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            pygame.draw.circle(window, (r, g, b), (mx, my), 50)
            pygame.display.update()

        # =================键盘事件====================
        if event.type == pygame.KEYDOWN:
            print('按键被按下', event.key, chr(event.key))
            if chr(event.key) == 'f':
                print('闪现')

            text = font.render(chr(event.key), True, (255, 0, 0))
            # window.fill((255, 255, 255))
            window.blit(text, (tx, 300))
            tx += 15
            pygame.display.update()
        if event.type == pygame.KEYUP:
            print('按键弹起')
