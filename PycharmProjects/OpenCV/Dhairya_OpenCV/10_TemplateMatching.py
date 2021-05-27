import numpy as np
import cv2

img = cv2.imread("opencv-template-matching-python-tutorial[1].jpg")
template = cv2.imread("opencv-template-for-matching[1].jpg",0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
w,h = template.shape[::-1]
#w=width h=height
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#match template returns a gray element so we convrt image to gray
#arg:: image, template, matching-method
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w, pt[1]+h),(255,255,0),4)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()