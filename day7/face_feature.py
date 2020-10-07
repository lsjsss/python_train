from PIL import Image, ImageDraw
import face_recognition

# 加载图片
image = face_recognition.load_image_file("faces_data\\ycd.jpg")

# 找出所有的面部特征
face_landmarks_list = face_recognition.face_landmarks(image)
print("face_landmarks_list", face_landmarks_list)
print("I found {} faces in this photograph", format(len(face_landmarks_list)))

pil_image = Image.fromarray(image)
print("pil_image", pil_image)
d = ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:
    for facial_feature in face_landmarks.keys():
        print("the {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

    for facial_feature in face_landmarks.keys():
        d.line(face_landmarks[facial_feature], width = 3)

pil_image.show()



