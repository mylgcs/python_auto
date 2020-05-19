import pygame

pygame.init()
window = pygame.display.set_mode((400, 600))
pygame.display.set_caption('显示图片')
# 设置背景颜色
window.fill((255, 255, 255))

# ==============显示文字============
# 1. 创建字体对象
# Font(字体文件路径, 字号)
font = pygame.font.Font('files/bb.ttf', 30)

# 2. 创建文字对象
# render(文字内容, True, 文字颜色, 背景颜色)
text = font.render('游戏你好', True, (255, 0, 0), (255, 255, 0))

# 3. 渲染到窗口上
window.blit(text, (0, 0))

# 4. 操作文字对象
# 1) 获取大小
w, h = text.get_size()
window.blit(text, (400-w, 600-h))

# 2) 缩放和旋转
new_t1 = pygame.transform.scale(text, (400, 50))
window.blit(new_t1, (0, 60))

new_t2 = pygame.transform.rotozoom(text, 90, 2)
window.blit(new_t2, (0, 120))

# 刷新
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
