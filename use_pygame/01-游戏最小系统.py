import pygame

# 1. 初始化操作
pygame.init()

# 2. 创建游戏窗口
# set_mode(大小)
window = pygame.display.set_mode((600, 400))
# 设置游戏标题
pygame.display.set_caption('余婷的游戏')


# 3. 让游戏保持一直运行的状态
# game loop (游戏循环 )
while True:
    # 4. 检测事件
    for event in pygame.event.get():
        # 检测关闭按钮被点击的事件
        if event.type == pygame.QUIT:
            # 退出
            exit()
