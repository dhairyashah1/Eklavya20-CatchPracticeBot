import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('2.JPG')
img2 = cv2.imread('Python_logo.PNG')
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret , mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
#if pixel value is above 220 converted to 255(white) else to black:
#black white --binary  #ret is boolean
mask_inv = cv2.bitwise_not(mask) # places having no mask in
#basically this is the reverse of mask(not gate)

#background
img1_bg = cv2.bitwise_and(roi, roi, mask= mask_inv) #and between roi and mask
#foreground
img1_fg = cv2.bitwise_and(img2,img2,mask = mask) #and betwwen img 2 n mask

dst = cv2.add(img1_bg,img1_fg)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('dst',dst)
img1[0:rows, 0:cols] = dst
cv2.imshow('img1',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()