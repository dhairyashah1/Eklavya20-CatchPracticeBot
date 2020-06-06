import numpy as np
import cv2
#red detection
vid = cv2.VideoCapture(0)  #Webcam=0
while True:
    _, frame = vid.read() #_ is used for those returned things whch are of no use
    # HSV = HUE, SATURATION, VALUE
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,70,50])  #provides a range
    upper_red = np.array([50,255,255])  # whatever pixels are in this range diaplay their color e
    #else they turn black
    mask = cv2.inRange(hsv,lower_red,upper_red)  #creating a range mask is in black n white
    #white in mask AND pixels in frame ==pixels in frame ....rest are black
    result = cv2.bitwise_and(frame,frame,mask = mask)
    cv2.imshow('frame',frame)
    cv2.imshow('hsv',hsv)
    cv2.imshow('maskrange',mask)
    cv2.imshow('result', result)
    if cv2.waitKey(5) & 0xFF == 27:
        break
vid.release()
cv2.destroyAllWindows()