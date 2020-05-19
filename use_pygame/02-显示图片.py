import pygame

pygame.init()
window = pygame.display.set_mode((400, 600))
pygame.display.set_caption('显示图片')
# 设置背景颜色
window.fill((255, 255, 255))
# ===========游戏开始页面静态效果=============
# 1. 加载图片
image1 = pygame.image.load('files/宝儿姐.jpg')
# 2. 渲染图片
# blit(渲染对象, 坐标)
window.blit(image1, (0, 0))

# 3. 操作图片
# 1) 获取图片大小
w, h = image1.get_size()
# print(w, h)
window.blit(image1, (400-w, 600-h))

# 2) 旋转和缩放
# scale(缩放对象, 目标大小)  - 可能会发生形变
new1 = pygame.transform.scale(image1, (100, 200))
window.blit(new1, (210, 0))

# rotozoom(缩放/旋转对象, 旋转角度, 缩放比例)
new2 = pygame.transform.rotozoom(image1, 180, 0.8)
window.blit(new2, (0, 200))

# 3.刷新显示页面
# pygame.display.flip()     - 第一次刷新
# pygame.display.update()   - 第一次以后的刷新
pygame.display.flip()


while True:
    # ==============游戏帧刷新==============
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
