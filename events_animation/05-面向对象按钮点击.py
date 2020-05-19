import pygame

from events_animation.button import Button

WIN_WIDTH = 400    # 窗口宽度
WIN_HEIGHT = 600   # 窗口高度

# 初始化游戏
pygame.init()

# 创建窗口
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('动画原理')
window.fill((255, 255, 255))
pygame.display.flip()

# 确定按钮
sure_button = Button('确定', (100, 100), (100, 50), (255, 0, 0), (255, 255, 255))
sure_button.draw(window)

button2 = Button('取消', (100, 200), (100, 50), (0, 255, 0), (255, 255, 255))
button2.draw(window)

button3 = Button('删除', (300, 200), (80, 40), (255, 255, 0), (0, 0, 0), 15)
button3.draw(window)

pygame.display.update()

while True:
    # 检测事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sure_button.is_down(event.pos, window):
                print('确定按钮被点击')

            if button2.is_down(event.pos, window):
                print('取消按钮')
        if event.type == pygame.MOUSEBUTTONUP:
            sure_button.is_up(event.pos, window)
            button2.is_up(event.pos, window)
