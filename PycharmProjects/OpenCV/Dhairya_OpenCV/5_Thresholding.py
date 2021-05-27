import numpy as np
import cv2

img = cv2.imread('CamscanImg.jpeg')
retval,threshold = cv2.threshold(img,75,255,cv2.THRESH_BINARY)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2 = cv2.threshold(gray,75,255,cv2.THRESH_BINARY)
adap = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,129,13)
cv2.imshow('img',img)
cv2.imshow('gray', gray)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('adap', adap)


cv2.waitKey(0)
cv2.destroyAllWindows()