import os
import os.path

# 允许加载的图片类型
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
"""
根据 knn 算法训练一个人脸识别模型，train_dir 包括的是每一个已知人名子目录以及名字，
model_save_path 表示模型训练好要保存的路径，n_neighbors 表示邻居的数量，也就是 K 值，
knn_algo 是模型选择的算法，返回值是根据所给的数据训练好的 knn 分类器
"""


def train(train_dir, model_save_path=None, n_neighbors=None, knn_algo="ball_tree", verbose=False):
    pass


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
