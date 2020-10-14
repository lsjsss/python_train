import cv2 as cv
import numpy as np


# 开启摄像头
def video_start():
    capture = cv.VideoCapture(0)                # 开启摄像头
    while True:
        ret, image = capture.read()
        image = cv.flip(image, 1)               # 图像反转
        dst = gaussian_blur(image)
        # dst = shift(image)              # 镜头效果
        cv.imshow("video", dst)

        key = cv.waitKey(10)
        if key == ord('j'):  # 镜头效果
            dst = gaussian_blur(image)
            cv.imshow("video", dst)


        key = cv.waitKey(10)
        if key == ord('m'):  # 水彩效果
            dst = shift(image)
            cv.imshow("video", dst)

        key = cv.waitKey(10)
        if key == ord('q'):                     # 按q键退出
            print("over")
            break


# -------------效果示例------------------
# 平面模糊效果
def blur(image):
    dst = cv.blur(image, (15, 1))      # 水平模糊， 竖直模糊
    return dst


# 中值模糊效果
def median_blur(image):
    dst = cv.medianBlur(image, 15)
    return dst


# 均值模糊效果
def custom_blur(image):
    kernel = np.ones([5, 5], np.float32)/25
    dst = cv.filter2D(image, -1, kernel=kernel)
    return dst


# 高斯模糊效果
def gaussian_blur(image):
    dst = cv.GaussianBlur(image, (15, 15), 50)     # 15x15
    return dst


# 美颜效果
def beauty(image):
    dst = cv.bilateralFilter(image, 0, 100, 13)
    return dst


# 水彩画效果
def shift(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    return dst


# 图片对比度增强
def equal_hist(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    return dst


# 局部对比增强
def clahe(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    return dst


# 阈值 强
def threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binaty = cv.threshold(gray, 127, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    return binaty


# 阈值
def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binaty = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 10)
    return binaty


# 边缘检测
def sobel_x(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    gradx = cv.convertScaleAbs(grad_x)
    return gradx


def sobel_y(image):
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    grady = cv.convertScaleAbs(grad_y)
    return grady


# 分离
def lapalian(image):
    dst = cv.Laplacian(image, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    return lpls


# 黑白边缘检测
def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)     # 高斯模糊
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    edge_output = cv.Canny(gray, 50, 150)
    return edge_output


# 彩色边缘检测
def color_edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)     # 高斯模糊
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    edge_output = cv.Canny(gray, 50, 150)
    dst = cv.bitwise_and(image, image, mask=edge_output)
    return dst


if __name__ == "__main__":
    video_start()
    cv.destroyAllWindows()