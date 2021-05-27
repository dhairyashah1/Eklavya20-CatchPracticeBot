import cv2
import numpy as np

vid = cv2.VideoCapture(0)
while True:
    _, frame = vid.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,70,50])
    upper_red = np.array([50,255,255])
    mask = cv2.inRange(hsv,lower_red, upper_red) #black n white required area mask rest black
    res = cv2.bitwise_and(frame ,frame, mask= mask) #mask and with frame original pic
    kernel = np.ones((15,15),np.float64)/225  #averaging divided ny the pdt of size
    #smooth
    smoothed = cv2.filter2D(res,-1,kernel)

    # types of blur: Gaussian blur, median blur, bilateral filter
    gaus = cv2.GaussianBlur(res,(15,15),9) #sigmaX - deviation in x
    median = cv2.medianBlur(res,15)
    bilateral = cv2.bilateralFilter(res,15,75,75)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('gaus',gaus)
    cv2.imshow('median ', median)
    cv2.imshow('bilateral', bilateral)

    if cv2.waitKey(5) & 0xFF ==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()