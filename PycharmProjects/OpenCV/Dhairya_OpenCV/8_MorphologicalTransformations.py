import numpy as np
import cv2

vid = cv2.VideoCapture(0)
while True:
    _, frame = vid.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 70, 50])
    upper_red = np.array([50, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask=mask)
    kernel = np.ones((1,1), np.uint8) #unsigned int has whole nos from 0 to 255
    erosion = cv2.erode(res,kernel,iterations = 2)
    dilation= cv2.dilate(erosion,kernel,iterations=2)
    #opening is combination of erosion followed by dilation
    opening = cv2.morphologyEx(res,cv2.MORPH_OPEN,kernel)
    #closing is combination of dilation followed by erosion
    closing = cv2.morphologyEx(res,cv2.MORPH_CLOSE,kernel)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)

    if cv2.waitKey(5) & 0xFF==27:
        break
vid.release()
cv2.destroyAllWindows()