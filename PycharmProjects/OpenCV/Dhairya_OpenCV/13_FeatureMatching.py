import cv2
import numpy as np
import matplotlib.pyplot as plt

#considering both as templates
img1 = cv2.imread("opencv-feature-matching-image.jpg",0)
img2 = cv2.imread("opencv-feature-matching-template.jpg",0)

#ORB = Oriented FAST and BRIEF Detector
#creating orb object
orb = cv2.ORB_create()

#keypoints and descriptors
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2, None)

#brute force object(main thing) matches features
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
#NORM_HAMMING is  the method

#finding matches
matches = bf.match(des1,des2)

#sorting matches ::most matching to least matching
matches = sorted(matches ,key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,
               matches[:10],None,flags=2)
plt.imshow(img3)
plt.show()