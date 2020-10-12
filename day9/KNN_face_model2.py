"""
根据KNN算法,训练一个人脸识别模型,train_dir包括的是每一个已知的子目录和他的名字
model_save_path表示模型训练好要保存的路径
n_neighbors
knn_algo是模型选择的算法,返回值是根据所给的数据训练好的knn分类器

"""
import os
import os.path
from PIL import Image, ImageDraw
import math
from sklearn import neighbors
import pickle
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder

# 允许加载的图片类型
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def train(train_dir, model_save_path=None, n_neighbors=None, knn_algo="ball_tree", verbose=False):
    # 设定输入输出值
    x = []
    y = []
    # 循环遍历训练集中的每个人
    for class_dir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir, class_dir)):
            continue
        # 循环遍历当前人员的每个图片
        for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
            image = face_recognition.load_image_file(img_path)
            face_bounding_boxes = face_recognition.face_locations(image)
            if len(face_bounding_boxes) != 1:
                if verbose:
                    if len(face_bounding_boxes) < 1:
                        print("Image {} not suitable for training:{}".format(img_path, "Did not find a face"))
                    else:
                        print("Image {} not suitable for training:{}".format(img_path, "Found more than one face"))
            else:
                # 为训练集添加当前的人脸数据
                x.append(face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0])
                print("x", x)
                y.append(class_dir)
                print("y", y)
    # 确定K值
    if n_neighbors is None:
        n_neighbors = int(round(math.sqrt(len(x))))
        print(len(x))
        if verbose:
            print("Chose n_neighbors automatically:", n_neighbors)

    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
    knn_clf.fit(x, y)

    # 保存到训练好的KNN分类器
    if model_save_path is not None:
        with open(model_save_path, "wb") as f:
            pickle.dump(knn_clf, f)

    return knn_clf


# train("knn_model_faces\\train", model_save_path="trained_model_clf", n_neighbors=2)

"""
用训练好的分类器来做测试
x_img_path:将要识别的图片路径
distance_threshold:距离阈值,值越大越马虎,容易误判
返回值就是图像中已识别的人脸的名称以及人脸位置列表

"""


def predict(x_img_path, knn_clf=None, model_path=None,
            distance_threshold=0.6):
    if not os.path.isfile(x_img_path) or os.path.splitext(x_img_path)[1][1:] not in ALLOWED_EXTENSIONS:
        raise Exception("Invalid image path:{}".format(x_img_path))

    # 加载训练好的模型
    if knn_clf is None:
        with open(model_path, 'rb') as f:
            knn_clf = pickle.load(f)

    # 加载图像文件并查找人脸位置
    x_img = face_recognition.load_image_file(x_img_path)
    x_face_locations = face_recognition.face_locations(x_img)

    # 如果没有找到人脸,我们就返回一个空值
    if len(x_face_locations) == 0:
        return []
    # 在测试集当中找到人脸特征
    face_encodings = face_recognition.face_encodings(x_img, known_face_locations=x_face_locations)

    # 用确定好的Knn模型为测试集人脸做最好的匹配
    closest_distance = knn_clf.kneighbors(face_encodings, n_neighbors=1)

    are_matches = [closest_distance[0][i][0] <= distance_threshold for i in range(len(x_face_locations))]
    print("are_matches", are_matches)


predict("knn_model_faces\\train\\Bob\\image_0001.jpg", model_path="trained_model_clf")


# 显示人脸识别的结果
# 参数:图片路径和预测值
def show_prediction_labels_on_image(img_path, predictions):
    pass


if __name__ == "__main__":
    pass
