# 导入 OS 模块
import os

# 导入 numpy 模块，用于做矩阵的运算
import numpy

# 导入 cv 模块
import cv2 as cv

# sklearn 进行数据的预处理
import sklearn.preprocessing as sp

# 建立一个人脸追踪器
face_detector = cv.CascadeClassifier("haar\\face.xml")

# 定义方法，来读取图片文件
def read_data(dirctory):
    # 判断是否为文件夹
    if not os.path.isdir(dirctory):
        raise IOError("The directory", dirctory, "does not exist")

    # 用户来存储人脸的数据
    faces_dir = {}

    # curdir 表示当前目录， subdir 表示当前目录下的所有子目录
    for cur,subdir,files, in os.walk(dirctory):











