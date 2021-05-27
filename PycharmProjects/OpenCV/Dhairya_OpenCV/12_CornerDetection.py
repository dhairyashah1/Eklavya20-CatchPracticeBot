import numpy as np
import cv2

img = cv2.imread("CornerDetectionImg.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corners = cv2.goodFeaturesToTrack(image=gray,maxCorners=300,
                                  qualityLevel=0.6,minDistance=3)
corners = np.int0(corners)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img,(x,y),3,(0,255,0),-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()