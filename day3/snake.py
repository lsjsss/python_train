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
BGCOLOR = Black

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
    DISPLAYSURE = pygame.display.set_mode((window_width, window_height))
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

        # 将新增加的一块保存到蛇身的列表当中
        wormCoords.insert(0, newHead)

        # 重新填充背景颜色
        DISPLAYSURE.fill(BGCOLOR)

        # 绘制方格
        drawGrid()

        # 将蛇身所在的位置的所有方块绘制成绿色
        drawWorm(wormCoords)

        # 食物绘制成红色
        drawApple(apple)

        # 游戏分数
        drawScore(len(wormCoords) - 3)

        # 更新窗口显示
        pygame.display.update()

        # 更新蛇的速度
        snake_speedClock.tick(snake_speed)


# 在游戏的右下角绘制显示消息
def drawPressKeyMsg():
    pass


# 在游戏的右下角绘制显示消息
def drawPressKeyMsg():
    # 设置绘制提示消息"按任意键进入与游戏"，白色字体
    pressKeySurf = BASICFONT.render('press any key to enter the game', True, white)

    # 设置提示信息显示位置(左上角)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (window_width - 200, window_height - 30)

    # 绘制游戏消息到提示窗口
    DISPLAYSURE.blit(pressKeySurf, pressKeyRect)


# 检查按键抬起事件
def checkForKeyPress():
    # 如果发现关闭了游戏窗口，直接退出游戏
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    KeyUpEvents = pygame.event.get(KEYUP)
    if len(KeyUpEvents) == 0:
        return None

    # 按下 ESC 键
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()

    # 返回按键事件对应的键值
    return KeyUpEvents[0].key


# 显示游戏刚进入时的欢迎界面
def showStartScreen():
    # 设置字体
    titleFont = pygame.font.Font('freesansbold.ttf', 48)

    # 渲染要显示的文本
    titleSurf = titleFont.render("interesting  Snake", True, White, DarkGreen)

    # 初始化欢迎画面的改变角度
    degrees = 0
    while True:
        # 设置背景颜色
        DISPLAYSURE.fill(BGCOLOR)
        #  将要显示的文本进行旋转一定的角度，显示在窗口上
        rotatedSurf1 = pygame.transform.rotate(titleSurf, degrees)
        rotatedRect1 = rotatedSurf1.get_rect()

        # 居中处理
        rotatedRect1.center(window_width / 2, window_height / 2)

        DISPLAYSURE.blit(rotatedSurf1, rotatedRect1)
        drawPressKeyMsg()

        # 检测到有按键按下时返回，退出欢迎界面
        if checkForKeyPress():
            # 清空事件列表
            pygame.event.get()
            return

        # 更新界面显示
        pygame.display.update()

        # 设置一个时钟，影响欢迎界面的旋转速度
        snake_speedClock.tick(20)

        # 每帧旋转 3 度
        degrees += 3


# 终止游戏程序
def terminate():
    # 卸载 pygame 中的游戏模块
    pygame.quit()

    # 系统退出
    sys.exit()


# 获取一个随机位置
def getRandomLocation():
    return {"x": random.randint(0, cell_width - 1),
            "y": random.randint(0, cell_height - 1)}

# 显示游戏结束的画面
def showGameOverScreen():
    # 渲染游戏结束时的文本
    gameOverFont = pygame.font.Font("freesansbold.ttf", 100)
    gameSurf = gameOverFont.render('Game', True, White)
    overSurf = gameOverFont.render('Over', True, White)

    # 文本显示所需要的区域
    gameRect = gameSurf.get_rect
    overRect = overSurf.get_rect
    
    # 文本显示位置的设置
    gameRect.midtop = (window_width / 2, 10)
    gameRect.midtop = (window_width / 2, gameRect)
    
    # 绘制文本到相应位置
    DISPLAYSURE.blit(gameSurf, gameRect)
    DISPLAYSURE.blit(overSurf, overRect)

    # 按下任意键开始游戏
    drawPressKeyMsg()

    # 更新窗口界面显示
    pygame.display.update()

    # 设置画面等待时间 500ms
    pygame.time.wait(500)

    # 清除事件当中的任何按键
    checkForKeyPress()

    # 循环等待用户新的按键
    while 1:
        if checkForKeyPress():
            pygame.event.get()
            return


# 绘制游戏的得分情况
def drawScore(score):
    # 渲染游戏分数的位置
    scoreSurf = BASICFONT.render("Score:%s" % (score), True, White)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (window_width - 120, 10)

    # 显示游戏分数到游戏窗口
    DISPLAYSURE.blit(scoreSurf, scoreRect)


# 进蛇身每个位置的方块绘制成绿色
def drawWorm():
    # 遍历蛇身的每个方块
    for coord in wormCoords:
        x = coord['x'] * cell_size
        y = coord['x'] * cell_size

        # 蛇身绘制成绿色
        wormSegmentRect = pygame.Rect(x, y, cell_size)
        pygame.draw.rect(DISPLAYSURE, DarkGreen, wormSegmentRect)

        # 绘制蛇身内边框
        wormInnersSegmentrect = pygame.Rect(
            x + 4, y + 4, cell_size - 8, cell_size - 8
        )

        pygame.draw.rect(DISPLAYSURE, Green, wormInnersSegmentrect)


# 绘制食物，将参数的位置绘制成红色，表示食物
def drawApple(coord):
    x = coord['x' * cell_size]
    y = coord['x' * cell_size]
    appleRect = pygame.Rect(x, y, cell_size)
    pygame.draw.rect(DISPLAYSURE, Red, appleRect)


# 绘制游戏地图
def drawGrid():
    # 在游戏窗口绘制灰色竖线
    for x in range(0, window_width, cell_size):
        pygame.draw.line(DISPLAYSURE, DarkGreen, DarkGray, (x, 0), (x, window_width))


    # 在游戏窗口绘制暗灰色横线
    for y in range(0, window_height, cell_size):
        pygame.draw.line(DISPLAYSURE, DarkGreen, DarkGray, (0, y), (window_height, y))


# 调用主函数，运行游戏
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass




































