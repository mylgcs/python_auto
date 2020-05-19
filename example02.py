"""
界面元素的显示
"""
import pygame

# 初始化游戏
pygame.init()

# 创建游戏窗口
# set_mode((宽度, 高度))   -  返回Surface对象
window = pygame.display.set_mode((800, 600))
# 设置标题
pygame.display.set_caption('游戏最小系统')
# 设置背景颜色
# (red, green, blue)
window.fill((255, 255, 255))
print('窗口大小:', window.get_size())

# ================游戏的第一个页面===============
# 1. 显示图片
# 1) 加载图片
# load(图片地址)  -  返回图片对应的Surface对象
img1 = pygame.image.load('resources/宝儿姐.jpg')
# 2) 显示图片
# blit(Surface对象, 位置)
# blit(Surface对象, (x坐标, y坐标))
img_w, img_h = img1.get_size()
print('图片大小:', img_w, img_h)
y = 100
x = 50
window.blit(img1, (x, y))
pygame.display.update()    # 更新界面的显示(凡是对游戏页面进行了修改都要进行这样一个更新的操作)

# 2. 显示文字
# 1) 创建字体对象(准备笔)
# Font(字体文件路径, 字体大小)   - 返回字体对象
ft = pygame.font.Font('resources/bb.ttf', 40)
# 2) 创建文字对象
# render(文字内容, True, 文字颜色, 文字背景颜色=None)   -  返回文字对应的Surface对象
title = ft.render('你好，pygame', True, (0, 0, 255), (255, 255, 0))
title2 = ft.render('开始', True, (255, 0, 0))
# 3) 显示文字
window.blit(title, (200, 20))
window.blit(title2, (300, 100))


# 3.画图形
# circle(窗口对象, 颜色, 圆心, 半径, 线宽=0)
pygame.draw.circle(window, (175, 238, 238), (300, 200), 50)
pygame.display.update()

# 游戏循环
num = 0
while True:
    num += 1
    if num % 100 == 0:
        x += 0.5
        window.fill((255, 255, 255))
        window.blit(title, (200, 20))
        window.blit(title2, (300, 100))
        pygame.draw.circle(window, (175, 238, 238), (300, 200), 50)
        if x >= 800-img_w:
            x = 800-img_w
        window.blit(img1, (x, y))
        pygame.display.update()

    # ==================游戏帧的刷新=================
    # 不断检测是否有事件发生
    for event in pygame.event.get():
        # 只要有事件发生这个for里面的代码就会执行，没有事件发生就不会执行
        num += 1
        # print('检测到事件', num)
        if event.type == pygame.QUIT:
            exit()
