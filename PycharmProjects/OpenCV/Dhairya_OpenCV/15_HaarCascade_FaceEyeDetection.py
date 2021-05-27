import cv2
import numpy as np
#face and eye detction using Haar Cascade Algorithm
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
vid = cv2.VideoCapture(0)
while True:
    _, frame = vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)
        cv2.imshow('frame',frame)
    if cv2.waitKey(30) & 0xFF ==27:
        break

vid.release()
cv2.destroyAllWindows()