import random
import pygame
import sys
from pygame.locals import *

# 设置初始速度
snake_speed = 5

# 设置窗口大小
window_width = 800
window_height = 600

# 地图单元格的宽和高度
cell_size = 20

# 断言测试，确保单元格可以窗口大小完美契合，即保证窗口能包含整数个单元格，
assert window_width % cell_size == 0, "Window width must be a multiple of cell size."
assert window_height % cell_size == 0, "Window height must be a multiple of cell size."

# 初始化水平和垂直方向单元格个数
cell_weight = int(window_width / cell_size)  # Cell Width
cell_height = int(window_height / cell_size)  # Cellc Height

# 定义游戏元素的颜色
White = (255, 255, 255)  # 白色
Black = (0, 0, 0)  # 黑色
Red = (255, 0, 0)  # 红色
Green = (0, 255, 0)  # 绿色
DARKGreen = (0, 155, 0)  # 暗绿色
DARKGRAY = (40, 40, 40)  # 暗灰色

#  设置游戏背景颜色（黑色）
BGCOLOR = Black  # Background color

# 设置游戏控制的键盘按键
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# 设置蛇头索引
HEAD = 0  # Syntactic sugar: index of the snake's head


# 定义游戏主函数
def main():
    # 声明全局变量
    global snake_speedCLOCK, DISPLAYSURF, BASICFONT
    # 初始化pygame模块
    pygame.init()
    # 初始化游戏时钟，影响蛇移动速度
    snake_speedCLOCK = pygame.time.Clock()
    # 初始化窗口分辨率
    DISPLAYSURF = pygame.display.set_mode((window_width, window_height))
    # 初始化字体
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    # 设置当前窗口标题
    pygame.display.set_caption('趣味贪吃蛇')
    #  显示进入游戏时的开发画面
    showStartScreen()

    # 循环运行游戏
    while True:
        runGame()
        showGameOverScreen()


# 游戏运行函数
def runGame():
    # 设置一个随机开始点（蛇的初始位置）.
    startx = random.randint(5, cell_weight - 6)
    starty = random.randint(5, cell_height - 6)

    # 设置初始蛇身（列表）
    wormCoords = [{'x': startx, 'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    # 设置初始移动方向
    direction = RIGHT

    # 随机显示一个食物
    apple = getRandomLocation()

    # 循环控制游戏操作
    while True:  # main game loop
        # 事件循环处理，event.get:从队列中获取事件
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
                # ESC退出游戏
                elif event.key == K_ESCAPE:
                    terminate()

        # 检查蛇头是否撞到窗口边缘,如果撞到游戏结束
        if wormCoords[HEAD]['x'] == -1 or \
                wormCoords[HEAD]['x'] == cell_weight or \
                wormCoords[HEAD]['y'] == -1 or \
                wormCoords[HEAD]['y'] == cell_height:
            return  # game over
        # 检查蛇头是否撞到了自己，如果撞到游戏结束
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and \
                    wormBody['y'] == wormCoords[HEAD]['y']:
                return  # game over

        # 检查蛇是否吃到食物
        if wormCoords[HEAD]['x'] == apple['x'] \
                and wormCoords[HEAD]['y'] == apple['y']:
            # 吃到食物尾部不动，头部移动后会增加一块，相当于蛇身长了一块
            # 如果吃到食物在随机产生一个新的食物
            apple = getRandomLocation()  # set a new apple somewhere
        else:
            # 删除蛇身尾部一块，移动时会蛇身在头部增加一块，整体蛇身未变
            del wormCoords[-1]

        # move the worm by adding a segment in the direction it is moving
        # 向上移动，蛇头在 y坐标-1 位置增加
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'],
                       'y': wormCoords[HEAD]['y'] - 1}
        # 向下移动，蛇头在 y坐标+1 位置增加
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'],
                       'y': wormCoords[HEAD]['y'] + 1}
        # 向左移动，蛇头在 x坐标+1 位置增加一块
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1,
                       'y': wormCoords[HEAD]['y']}
        # 向左移动，蛇头在 x坐标+1 位置增加一块
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1,
                       'y': wormCoords[HEAD]['y']}
        # 将新增加的一块保存到蛇身的列表中
        wormCoords.insert(0, newHead)

        # 重新填充背景颜色
        DISPLAYSURF.fill(BGCOLOR)

        # 绘制方格（游戏地图）
        drawGrid()

        # 将蛇身所在位置所有方块绘制为绿色
        drawWorm(wormCoords)

        # 将食物所在位置绘制为红色
        drawApple(apple)

        # 显示游戏分数
        drawScore(len(wormCoords) - 3)

        # 更新窗口显示
        pygame.display.update()

        # 更新蛇的移动速度
        snake_speedCLOCK.tick(snake_speed)


# 在游戏右下角绘制提示消息
def drawPressKeyMsg():
    # 设置绘制提示消息内容“按任意键进入游戏”，白色字体
    pressKeySurf = BASICFONT.render('Press any key to enter the game.', True, White)
    # 设置提示消息的显示位置
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (window_width - 200, window_height - 30)
    # 绘制提示消息到游戏窗口
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


# 检查按键抬起事件
def checkForKeyPress():
    # 如果发现关闭了游戏窗口，直接退出游戏
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    # 获取按键抬起事件
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    # 如果按下ESC，
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    # 返回按键事件对应的键值
    return keyUpEvents[0].key


# 显示游戏刚进入时的欢迎画面
def showStartScreen():
    # 设置字体
    titleFont = pygame.font.Font('freesansbold.ttf', 48)
    # 渲染要显式的文本（白色字体，深绿色背景）
    titleSurf1 = titleFont.render('Interesting Snake!', True, White, DARKGreen)

    # 初始化欢迎画面每帧的改变角度
    degrees = 0
    while True:
        # 设置背景颜色
        DISPLAYSURF.fill(BGCOLOR)
        # 将要显式的文本进行旋转一定角度，在显示到窗口上
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (window_width / 2, window_height / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)
        drawPressKeyMsg()
        # 检查到有按键按下时返回，退出欢迎界面
        if checkForKeyPress():
            pygame.event.get()  # 清空事件列表，clear event queue
            return
        # 更新界面显示
        pygame.display.update()
        # 设置时钟，影响欢迎画面旋转的速度
        snake_speedCLOCK.tick(20)
        # 每帧旋转3度
        degrees += 3


# 终止游戏程序
def terminate():
    # 卸载 pygame 的所有模块
    pygame.quit()
    # 系统退出
    sys.exit()


# 获取一个随机位置
def getRandomLocation():
    return {'x': random.randint(0, cell_weight - 1),
            'y': random.randint(0, cell_height - 1)}


# 显示游戏结束的画面
def showGameOverScreen():
    # 渲染游戏结束时显示的文本
    gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
    gameSurf = gameOverFont.render('Game', True, White)
    overSurf = gameOverFont.render('Over', True, White)
    # 文本显示需要的矩形区域
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    # 文本显示位置
    gameRect.midtop = (window_width / 2, 10)
    overRect.midtop = (window_width / 2, gameRect.height + 10 + 25)
    # 绘制文本到相应位置
    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    # 绘制右下角的提示信息：按任意键开始游戏
    drawPressKeyMsg()
    # 更新窗口界面显示
    pygame.display.update()
    # 等待500毫秒，结束画面至少停留500毫秒
    pygame.time.wait(500)
    # 清除事件队列中的任何按键
    checkForKeyPress()  # clear out any key presses in the event queue

    # 循环等待用户按键事件
    while True:
        if checkForKeyPress():
            pygame.event.get()  # 清空事件列表，clear event queue
            return


# 绘制游戏分数
def drawScore(score):
    # 渲染游戏分数字体和位置
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, White)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (window_width - 120, 10)
    # 显示游戏分数到游戏窗口
    DISPLAYSURF.blit(scoreSurf, scoreRect)


# 将蛇身每个位置的方块绘制为绿色
def drawWorm(wormCoords):
    # 遍历蛇身的的每个方块
    for coord in wormCoords:
        x = coord['x'] * cell_size
        y = coord['y'] * cell_size
        # 将蛇身方法绘制位置绘制为绿色
        wormSegmentRect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(DISPLAYSURF, DARKGreen, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(
            x + 4, y + 4, cell_size - 8, cell_size - 8)
        pygame.draw.rect(DISPLAYSURF, Green, wormInnerSegmentRect)


# 绘制食物，将参数的方块位置绘制为红色，表示食物
def drawApple(coord):
    x = coord['x'] * cell_size
    y = coord['y'] * cell_size
    appleRect = pygame.Rect(x, y, cell_size, cell_size)
    pygame.draw.rect(DISPLAYSURF, Red, appleRect)


# 画栅格（游戏地图）
def drawGrid():
    # 在游戏窗口绘制暗灰色竖线
    for x in range(0, window_width, cell_size):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, window_height))
    # 在游戏窗口绘制暗灰色横线
    for y in range(0, window_height, cell_size):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (window_width, y))


# 调用主函数，运行游戏
if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass

# 扩展：增加
