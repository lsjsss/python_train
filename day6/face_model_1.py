# 导入 OS 模块
import os

# 导入 numpy 模块，用于做矩阵的运算
import numpy as np

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
    for curdir, subdir, files, in os.walk(dirctory):
        for jpeg in (
                file for file in files if file.endswith(".jpg")
        ):
            path = os.path.join(curdir, jpeg)
            # 读取图片路径
            print("path:", path)

            # 获取文件标签
            label = path.split(os.path.sep)
            # print(label)
            label = label[-2]

            # 如果字典当中没有 label 键，就创建一个新的 label 为键的字典
            if label not in faces_dir:
                # 读取每个文件夹中的第一个文件
                faces_dir[label] = [path]
            else:
                faces_dir[label].append(path)

    # 数据预处理
    codec = sp.LabelEncoder()
    codec.fit(list(faces_dir.keys()))

    x, y, z = [], [], []
    for label, filenames in faces_dir.items():
        for filename in filenames:
            # 局部二值模式，只能处理灰度图，进行灰度的转换
            bgr = cv.imread(filename)
            gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.1, 2, minSize=(100, 100))

            for l, t, w, h in faces:
                a, b = int(w / 2), int(h / 2)
                x.append(gray[t:t + h, l:l + w])
                y.append(int(codec.transform([label])[0]))
                cv.ellipse(bgr, (l + a, t + b), (a, b), 0, 0, 360, (255, 0, 255), 2)
                z.append(bgr)
    y = np.array(y)
    return codec, x, y, z


codec, train_x, train_y, train_z = read_data("faces\\training")
# print("codec", codec)
# print("*"*20)
# print("train_x", train_x)
# print("*"*20)
# print("train_y", train_y)
# print("*"*20)
# print("train_z", train_z)

_, test_x, test_y, test_z = read_data("faces\\testing")

# 用局部二值模式直方图建立人脸识别模型
model = cv.face.LBPHFaceRecognizer_create()
model.train(train_x, train_y)
pred_test_y = []
for x in test_x:
    y = model.predict(x)
    print(y)
    pred_test_y.append(y[0])

escape = False
while not escape:
    for code, pred_code, image in zip(test_y, pred_test_y, test_z):
        label = codec.inverse_transform([code])
        print("label:", label)
        label = label[0]
        pred_label = codec.inverse_transform([pred_code])[0]
        print("pred_label:", pred_label)

        text = "{}{}{}".format(label, "==" if label == pred_label else "!=", pred_label)
        cv.putText(image, text, (10, 60), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 6)
        cv.imshow("Recognizing Face....", image)

        if cv.waitKey(1000) == 27:
            escape = True
            break
