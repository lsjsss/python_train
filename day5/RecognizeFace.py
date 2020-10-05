import cv2 as cv

# 通过哈尔级联分建立五官追踪器
face_detecor = cv.CascadeClassifier("haar\\face.xml")
eye_detecor = cv.CascadeClassifier("haar\\eye.xml")
nose_detecor = cv.CascadeClassifier("haar\\nose.xml")









