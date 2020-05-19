"""
游戏最小系统
"""
import pygame

# 1.初始化游戏
pygame.init()

# 2.创建游戏窗口
# set_mode((宽度, 高度))   -  返回Surface对象
window = pygame.display.set_mode((800, 600))
# 设置标题
pygame.display.set_caption('游戏最小系统')


# 3.游戏循环
num = 0
while True:
    # 4.不断检测是否有事件发生
    for event in pygame.event.get():
        # 只要有事件发生这个for里面的代码就会执行，没有事件发生就不会执行
        num += 1
        print('检测到事件', num)
        if event.type == pygame.QUIT:
            exit()
