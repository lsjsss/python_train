import os
import os.path
import face_recognition
from face_recognition.face_detection_cli import image_files_in_folder

# 允许加载的图片类型
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
"""
根据 knn 算法训练一个人脸识别模型，train_dir 包括的是每一个已知人名子目录以及名字，
model_save_path 表示模型训练好要保存的路径，n_neighbors 表示邻居的数量，也就是 K 值，
knn_algo 是模型选择的算法，返回值是根据所给的数据训练好的 knn 分类器
"""


def train(train_dir, model_save_path=None, n_neighbors=None, knn_algo="ball_tree", verbose=False):
    # 设定输入输出值
    x = []
    y = []

    # 循环遍历训练集当中的每个人
    for class_dir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir)):
            continue
        # 循环遍历当前人员的每个训练图片
        for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
            image = face_recognition.load_image_file(img_path)
            face_bounding_boxes = face_recognition.face_locations(image)
            if len(face_bounding_boxes) != 1:
                if verbose:
                    if len(face_bounding_boxes) < 1:
                        print("Image {} not in suitable for train:{}", format(img_path, "Did not find a face"))
                    else:
                        print("Image {} not in suitable for train:{}", format(img_path, "Found more than one face"))
            else:
                # 为训练集添加当前的人脸特征数据
                x.append(face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0])
                print("x", x)
                y.append(class_dir)
                print("y", y)


train("knn_model_faces\\train")

"""
用训练好的分类器来做测试
x_img_path:将要识别的路径
distance_threshold：距离阈值，值越大，就越马虎,容易误判
返回值是图像中易识别的人脸的名称及人脸位置列表
"""


def predict(x_img_path, knn_clf=None, mode_path=None, distance_thresold=0.6):
    pass


# 显示人脸识别的结果
def show_prediction_labels_on_image(image_path, predictions):
    pass


if __name__ == "__main__":
    pass
