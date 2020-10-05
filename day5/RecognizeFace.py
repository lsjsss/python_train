import cv2 as cv

# 通过哈尔级联分建立五官追踪器
face_detector = cv.CascadeClassifier("haar\\face.xml")
eye_detecor = cv.CascadeClassifier("haar\\eye.xml")
nose_detecor = cv.CascadeClassifier("haar\\nose.xml")

# 打开摄像头
capt = cv.VideoCapture(0)
while 1:
    image = capt.read()[1]
    faces = face_detector.detectMultiScale(image, 1.3, 5)
    eyes = eye_detecor.detectMultiScale(image, 1.3, 5)
    noses = nose_detecor.detectMultiScale(image, 1.3, 5)
    print("faces:", faces)
    print("eyes:", eyes)
    print("noses:", noses)

    # 确定圆心目标，确定长短轴，进行画图确定五官
    for l,t,w,h in faces:
        a,b = int(w/2), int(h/2)
        cv.ellipse(image, (l + a, b + t), (a, b), 0, 0, 360, (255, 0, 13), 3)

    for l,t,w,h in eyes:
        a,b = int(w/2), int(h/2)
        cv.ellipse(image, (l + a, b + t), (a, b), 0, 0, 360, (134, 234, 102), 3)

    for l, t, w, h in noses:
        a, b = int(w / 2), int(h / 2)
        cv.ellipse(image, (l + a, b + t), (a, b), 0, 0, 360, (234, 0, 255), 3)

    cv.imshow("VIDEOCAPTURE", image)


    if cv.waitKey(33) == 27:
        break

# 关闭窗口
capt.release()
cv.destroyAllWindows()







