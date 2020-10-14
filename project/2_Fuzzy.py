import face_recognition
import cv2

'''
这是视频中人脸模糊的演示。请注意：此示例要求仅从网络摄像头读取时安装OpenCV（“ cv2”库）。
使用face_recognition库*不需要* OpenCV。仅当您要运行此特定演示时才需要。
如果您在安装它时遇到问题，请尝试其他不需要它的演示。获取对网络摄像头＃0的引用（默认值）

'''
video_capture = cv2.VideoCapture(0)

# 初始化一些变量
face_locations = []

while True:
    # 抓取一帧视频
    ret, frame = video_capture.read()

    # 将视频帧调整为1/4尺寸以加快人脸检测处理
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # 查找当前视频帧中的所有面部和面部编码
    face_locations = face_recognition.face_locations(small_frame, model="cnn")

    # 显示结果
    for top, right, bottom, left in face_locations:
        # 由于我们检测到的帧被缩放为1/4尺寸，因此应放大后脸的位置
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # 提取图像中包含面部的区域
        face_image = frame[top:bottom, left:right]

        # 模糊人脸图像
        face_image = cv2.GaussianBlur(face_image, (99, 99), 30)

        # 将模糊的脸部区域放回框架图像中
        frame[top:bottom, left:right] = face_image

    # 显示结果图像
    cv2.imshow('Video', frame)

    # 按键盘上的“ q”退出！
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放手柄到网络摄像头
video_capture.release()
cv2.destroyAllWindows()