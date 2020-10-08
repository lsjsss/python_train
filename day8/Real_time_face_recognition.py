# 打开摄像头
import cv2 as cv

# face_recognition 主要用来进行人脸特征的提取并且与身份确认
import face_recognition

video_capture = cv.VideoCapture(0)

# face_reconition 加载图片,命名时使用名字缩写
zwq_image = face_recognition.load_image_file("faces_data\\zwq1.jpg")

# 输出图片效果
print("zwq_image", zwq_image)

zhuyue_image = face_recognition.load_image_file("faces_data\\zhuyue1.jpg")
print("zhuyue_image", zhuyue_image)

# 通过图片数据对人脸特征进数据行识别提取
zwq_face_encoding = face_recognition.face_encodings(zwq_image)
zhuyue_face_encoding = face_recognition.face_encodings(zhuyue_image)

# 查看人脸特征信息
print("zwq_face_encoding", zwq_face_encoding)

# 建立列表存放人脸特征信息和对应的人名信息
known_face_encodings = [
    zwq_face_encoding,
    zhuyue_face_encoding
]

# 建立已知的姓名标签
known_face_names = [
    "ZWQ",
    "ZHUYUE"
]

# 初始化一些变量，
face_locations = []  # 用来获取人脸边框数据
face_encodings = []  # 获取摄像头前面在人脸特征信息
face_names = []  # 获取对应在人脸标签

process_this_frame = True
while True:
    ret, frame = video_capture.read()

    # 将视频帧缩放到四分之一比例，便于快速处理
    small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
    print("small_frame", small_frame)

    # 使用 opencv 处理图片，将颜色转换为 BGR
    rgb_small_frame = small_frame[:, :, :: -1]
    print("rgb_small_frame", rgb_small_frame)

    if process_this_frame:
        # 找到所有的人脸及人脸特征，获取动态人脸的边框数组
        face_locations = face_recognition.face_locations(rgb_small_frame)

        # 获取摄像头前的动态人脸数据
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        print("I Found {} face in this video".format(len(face_encodings)))
        face_names = []  # 存儲動態的人臉標簽

        # 獲取單個人臉的特徵數據
        for face_encoding in face_encodings:
            # 進行人臉比較
            matches = face_recognition.compare_faces(
                # matches 表示的是动态人脸数与数据库当中的人脸天特征数据匹配 tolerance 阈值大小
                known_face_encodings, face_encoding, tolerance=0.4
            )
            print("matches:", matches)

        if cv.waitKey(33) == 27:
            break

video_capture.release()
cv.destoryAllWindows()











