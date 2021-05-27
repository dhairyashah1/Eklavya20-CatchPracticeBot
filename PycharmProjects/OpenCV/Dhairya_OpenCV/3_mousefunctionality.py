import cv2
import numpy as np

ex , ey = -1 , -1
drawing = False

def draw_rect(event,x,y,flags,params):
    global ex, ey, drawing
    if event == cv2.EVENT_LBUTTONDOWN:  #button pressed
        ex , ey = x , y
        drawing = True
    elif event== cv2.EVENT_LBUTTONUP:  #button up
        drawing=False
        cv2.rectangle(img,
                      (ex,ey),
                      (x,y),
                      (255,0,0), #BGR code BLUE
                      -1)
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,
                          (ex, ey),
                          (x, y),
                          (0,255,0), #GREEN
                          -1)
#as left mouse button is pressed(BUTTONDOWN) rect of green color is generated as we release(BUTTONUP) it , it turns blue
#ex,ey=x,y are starting points(Drawing=True) : as the rect is drawn ex ,ey != x , y(Drawing=False)
#linking function to callback
cv2.namedWindow(winname='draw_1')

#callback
img = np.zeros((512,512,3),np.int8)
cv2.setMouseCallback('draw_1',draw_rect)

#using cv2 to show image
while True:
    cv2.imshow('draw_1',img)

    if cv2.waitKey(5) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()