#importing required libraries and modules
import cv2
import numpy as np
import matplotlib.pyplot as plt

#creating a function
#x, y, flags, param are feed to open cv automatically
def func_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
       #if event matches cv2 event(clicking leftmousebutton) the following would be implemented
       cv2.circle(img,
                   (x,y),
                    10,
                   (255,0,0),
                   -1)
    #for right click
    elif event== cv2.EVENT_RBUTTONUP:
        cv2.circle(img,
                   (x,y),
                   25,
                   (255,255,255),
                   3)

#connect the function with callback
cv2.namedWindow(winname="my_proj")

#callback
cv2.setMouseCallback('my_proj',func_circle)

#using open cv to show the image
 #creating a blank(black) image
img = np.ones((512,512,3),np.int8)
while True:
    cv2.imshow('my_proj',img)
    if cv2.waitKey(5) & 0xFF==27 : #quits drawing area on clicking esc :for other keys ord('a')
        break
cv2.destroyAllWindows()