import numpy as np
import cv2

vid = cv2.VideoCapture(0)
while True:
    _, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    laplacian2 = cv2.Laplacian(gray,cv2.CV_64F)

    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=1)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=-1)
    #Canny(Edge detection Algorithm)
    edges = cv2.Canny(frame,75,75)


    cv2.imshow('laplacian',laplacian)
    cv2.imshow('laplacian2',laplacian2)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edges',edges)

    if cv2.waitKey(5) & 0xFF==27:
        break
vid.release()
cv2.destroyAllWindows()