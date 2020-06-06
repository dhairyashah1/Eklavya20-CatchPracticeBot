import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("GrabCut_FaceImg.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
rectangle = (165,55,100,160)
mask = np.zeros(img.shape[:2],np.uint8)
bg_model = np.zeros((1,65),np.float64)
fg_model = np.zeros((1,65),np.float64)
grab = cv2.grabCut(img=img,mask=mask,rect=rectangle,bgdModel=bg_model,
                   fgdModel=fg_model,iterCount=5,mode=cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==0)|(mask==2),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()