import cv2
import numpy as np
import matplotlib.pyplot as plt

vid = cv2.VideoCapture(0) #0 for webcam and 'path' for present video
fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
    _, frame = vid.read()
    fgbg_mask = fgbg.apply(frame)
    #kernel = np.array([3,3],np.float32)
    #fgbg_mask = cv2.morphologyEx(fgbg_mask,cv2.MORPH_OPEN,kernel)
    #optional to remove flash
    cv2.imshow('frame',frame)
    cv2.imshow('fgbg_mask',fgbg_mask)

    if cv2.waitKey(5) & 0xFF==27:
        break

vid.release()
cv2.destroyAllWindows()
