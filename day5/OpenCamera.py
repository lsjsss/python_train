import cv2 as cv

# 打开摄像头
capt = cv.VideoCapture(0)
print(capt)

while 1:
    # image 为一个元组，(True, 三维数组, 数组类型)    [1]为索引
    image = capt.read()[1]
    print(image)

    # 窗口显示
    image = cv.resize(image, None, fx = 0.8, fy = 0.8, interpolation = cv.INTER_AREA)
    cv.imshow("VideoCapter", image)

    # 设置退出机制，按下ESC退出程序
    if cv.waitKey(33) == 27:
        break

# 主要释放已经调用的摄像头，避免下次调用的失误(关闭窗口)
capt.release()
cv.destroyAllWindows()




