import face_recognition
import cv2
import cv2 as cv
from PIL import Image, ImageDraw

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

        # 查找图像中所有面部的所有面部特征
        face_landmarks_list = face_recognition.face_landmarks(face_image)

        # 从导出阵列接口的对象创建一个图像存储器
        pil_image = Image.fromarray(face_image)

        # 遍历面部特征
        for face_landmarks in face_landmarks_list:
            # 设置图像填充模式为 RGBA, 对图像进行填充
            d = ImageDraw.Draw(pil_image, 'RGBA')

            # 画眉毛轮廓
            d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
            d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
            # 填充眉毛
            d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
            d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

            # 唇彩轮廓
            d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
            d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
            # 填充唇彩
            d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
            d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

            # 眼睛轮廓
            d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
            d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))
            # 绘制眼线
            d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
            d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

        # 将模糊后的脸部区域放回图像中
        frame[top:bottom, left:right] = pil_image

    # 显示结果图像
    cv2.imshow('Video', frame)

    # 按下ESC退出程序
    if cv.waitKey(33) == 27:
        break

# 释放已经调用的摄像头，避免下次调用的失误(关闭窗口)
video_capture.release()
cv2.destroyAllWindows()