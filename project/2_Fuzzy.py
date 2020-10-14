import face_recognition
import cv2
import cv2 as cv

'''
使用摄像头识别面部对面部进行模糊
'''

# 打开摄像头
video_capture = cv2.VideoCapture(0)

# 初始化面部位置变量
face_locations = []

while True:
    # 从视频中抓取一帧图像
    ret, frame = video_capture.read()

    # 调整图像大小，将视频帧调整为 1/4 尺寸以加快人脸检测处理
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # 查找当前视频帧中的所有面部和面部编码
    face_locations = face_recognition.face_locations(small_frame, model="cnn")

    # 显示模糊后的效果
    for top, right, bottom, left in face_locations:
        # 由于检测到的帧被缩放为1/4尺寸，因此应放大后脸的位置，还原图像
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # 提取图像中包含面部的区域
        face_image = frame[top:bottom, left:right]

        # 使用高斯模糊模糊人脸图像
        face_image = cv2.GaussianBlur(face_image, (99, 99), 30)

        # 将模糊后的脸部区域放回图像中
        frame[top:bottom, left:right] = face_image

    # 显示结果图像
    cv2.imshow('Video', frame)

    # 按下ESC退出程序
    if cv.waitKey(33) == 27:
        break

# 释放已经调用的摄像头，避免下次调用的失误(关闭窗口)
video_capture.release()
cv2.destroyAllWindows()
