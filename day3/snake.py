import random
import pygame
import sys
from pygame.locals import *

# 设置贪吃蛇的初速度
snake_speed = 5

# 设置游戏窗口的大小，宽800，高600
window_width = 800
window_height = 600

# 设置地图单元格的宽度和高度
cell_size = 20

# 断言测试，确保单元格可以和窗口大小完整契合
assert window_width % cell_size == 0, "Window width must be a multiple of cell size"
assert window_height % cell_size == 0, "Window width must be a multiple of cell size"

# 初始化水平和垂直方向单元格个数
cell_width = int(window_width / cell_size)
cell_height = int(window_height / cell_size)

# 定义游戏元素的颜色
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
DarkGreen = (0, 155, 0)  # 暗绿色
DarkGray = (50, 50, 50)  # 暗灰色

# 设置游戏的背景颜色(黑色)
BGColor = Black

# 设置游戏键盘的控制按键
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

# 设置蛇头索引
HEAD = 0


# 定义游戏的主函数
def main():
    # 声明全局变量
    global snake_speedClock, DISPLAYSURE, BASICFONT
    # 初始化 pygame 的模块
    pygame.init()
    # 初始化游戏时钟，影响蛇移动的速度
    snake_speedClock = pygame.time.Clock()
    # 初始化窗口分辨率
    DISPLAYSURE = pygame.display.set_mode(window_width, window_height)
    # 字体的设置
    BASICFONT = pygame.font.Font('freesansblod.ttf', 18)
    # 设置当前窗口的标题
    pygame.display.set_caption("趣味贪吃蛇")
    # 显示进入游戏时的开始界面
    showStartScreen()
    # 循环运行游戏
    while 1:
        runGame()
        showGameOverScreen()


# 定义游戏的运行函数
def runGame():
    # 设置一个随机开始点
    startx = random.randit(5, cell_width - 6)
    starty = random.randit(5, cell_width - 6)

    # 设置初始蛇身[列表]
    wormCoords = [
        {'x': startx, 'y': starty},
        {'x': startx - 1, 'y': starty},
        {'x': startx - 2, 'y': starty},
    ]

    # 设置初始移动方向
    direction = RIGHT

    # 随机显示一个食物
    apple = getRandomLocation()

    # 循环控制游戏操作
    while 1:
        # 时间的循环处理机制，event.get:从队列当中获取事件
        for event in pygame.event.get():
            # 关闭窗口事件
            if event.type == QUIT:
                terminate()

            # 键盘按键事件
            elif event.type == KEYDOWN:
                # 向左移动
                if (event.key == K_LEFT) and direction != RIGHT:
                    direction = LEFT


                # 向右移动
                elif (event.key == K_RIGHT) and direction != LEFT:
                    direction = RIGHT


                # 向上移动
                elif (event.key == K_UP) and direction != DOWN:
                    direction = UP


                # 向下移动
                elif (event.key == K_DOWN) and direction != UP:
                    direction = DOWN


                # 终止游戏
                elif event.key == K_ESCAPE:
                    terminate()
        # 检查蛇头是否撞到边缘，如果撞到则游戏结束
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == cell_width or \
           wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['x'] == cell_height:
            return

        # 检查蛇头是否吃到食物
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            # 吃到食物以后尾部不动，头部增长一块，蛇身变长
            # 随机产生一个新的食物
            apple = getRandomLocation()
        else:
            del wormCoords[-1]

        # 向上移动，蛇头在 y 坐标上 -1，位置增加
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'],
                       'y': wormCoords[HEAD]['y'] - 1}

        # 向下移动，蛇头在 y 坐标上 +1，位置增加
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'],
                       'y': wormCoords[HEAD]['y'] + 1}

        # 向左移动，蛇头在 x 坐标上 -1，位置增加
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1,
                       'y': wormCoords[HEAD]['y']}

        # 向右移动，蛇头在 x 坐标上 +1，位置增加
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1,
                       'y': wormCoords[HEAD]['y']}





        # 在游戏的右下角绘制显示消息
def drawPressKeyMsg():
    pass


# 在游戏的右下角绘制显示消息
def drawPressKeyMsg():
    pass


# 检查按键抬起事件
def checkForKeyPress():
    # 如果发现关闭了游戏窗口，直接退出游戏
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    KeyUpEvents = pygame.event.get(KEYUP)
    if len(KeyUpEvents) == 0:
        return None

    # 返回按键事件对应的键值
    return KeyUpEvents[0].key


# 显示游戏刚进入时的欢迎界面
def showStartScreen():
    pass


# 终止游戏程序
def terminate():
    pass


# 获取一个随机位置
def getRandomLocation():
    pass


# 显示游戏结束的画面
def showGameOverScreen():
    pass


# 绘制游戏分数
def drawScore(score):
    pass


# 将蛇身每个位置的方块绘制成绿色
def drawWorm():
    pass


# 绘制食物，将参数的位置绘制成红色
def drawApple():
    pass


# 绘制游戏地图
def drawGrid():
    pass
