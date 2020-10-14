from PIL import Image, ImageDraw
import face_recognition

'''
图片美颜
'''
# 加载图片，将 jpg 文件加载到 numpy 数组中
image = face_recognition.load_image_file("F:\\PycharmProject\\python_train-2020.9\\day8\\faces_data\\ycd.jpg")

# 查找图像中所有面部的所有面部特征
face_landmarks_list = face_recognition.face_landmarks(image)

# 从导出阵列接口的对象创建一个图像存储器
pil_image = Image.fromarray(image)

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

    # 显示图像
    pil_image.show()
