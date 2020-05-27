
import cv2
import numpy as np
import matplotlib.pyplot as plt
#% matplotlib inline

black_img = np.zeros(shape=(512,512,3),   #creating a fully black image
               dtype=np.int16 )

#drawing a circle
cv2.circle(black_img,
           center =(100,100),
           radius=55,
           color=(255,0,245),
           thickness=8) #thickness is pixels outside inner radius(=55) circle

#drawing a filled circle
cv2.circle(black_img,  #or img = black_img
           center =(400,100),
           radius=55,
           color=(55,90,245),
           thickness=-1)

#drawing a rectangle --> 2 diagonal points(pt1,pt2) needed
#sidea are parallel to axes
cv2.rectangle(black_img,
              pt1=(100,500),
              pt2=(300,400),
              thickness=8,
              color=(255,255,255)
        )
#drawing a triangle
vertices = np.array([(50,350),
                    (200,350),
                    (100,200)],
                      np.int32)
pts = vertices.reshape(-1,1,2)
cv2.fillPoly(black_img,
              [pts],
            #  isClosed=True,
              color=(132,45,76))
          #    thickness=5)

#drawing a line
cv2.line(black_img,
         pt1=(400,512),
         pt2=(512,300),
         color=(0,255,12),
         thickness=4,
         lineType=cv2.LINE_4)

#inserting text
font = cv2.FONT_ITALIC
cv2.putText(black_img,
            text='shaah',
            org=(250,250),
            fontFace=font,
            fontScale=2.8,
            color=(123,255,34),
            thickness=3,
            lineType=cv2.LINE_AA)
plt.imshow(black_img)
plt.show()   #extra in pycharm