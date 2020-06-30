#Reference-https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/
# USAGE
# python detect.py --images images

# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import random
#from matplotlib import pyplot as plt

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="path to images directory")
args = vars(ap.parse_args())

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# loop over the image paths
imagePaths = list(paths.list_images(args["images"]))

for imagePath in imagePaths:
	# load the image and resize it to (1) reduce detection time
	# and (2) improve detection accuracy
	j=0
	i=j
	image = cv2.imread(imagePath)
	image = imutils.resize(image, width=min(400, image.shape[1]))
	orig = image.copy()

	# detect people in the image
	(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
		padding=(8, 8), scale=1.05)
	# draw the original bounding boxes
	for (x, y, w, h) in rects:
		cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)
		if i==j:#This ensures that only the first identified person gets the chance for catch since we can project only one projectile
			# creating rectangles on either sides of the person for selecting required random point for catching
			cv2.rectangle(image,(x-70,y+200),(x,y-100),(0,0,255),3)
			cv2.rectangle(image,(x+w-70,y+200),(x+w,y-100),(0,0,255),3)
			# Now we ensure that both rectangles are taken in to consideration for random point selection.
			x10=random.randrange(x-70,x,1)
			y10=random.randrange(y-100,y+200,1)
			x11=random.randrange(x+w-70,x+w,1)
			y11=random.randrange(y-100,y+200,1)
			# Final selection for random point
			x1=random.choice([x10,x11])
			if x1==x10:
				y1=y10
			else:
				y1=y11
			z1=1# Arbitarily assigning this value since we don't have the required depth data for now.
			i+=1
	cv2.circle(image,(x1,y1),10,(255,0,0),3)
	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

	# draw the final bounding boxes
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

	# show some information on the number of bounding boxes
	filename = imagePath[imagePath.rfind("/") + 1:]
	#print("[INFO] {}: {} original boxes, {} after suppression".format(
	#	filename, len(rects), len(pick)))

	# show the output images
	j+=1
	row,col,ch=image.shape
	#cv2.imshow("Before NMS", orig)
	cv2.imshow("After NMS", image)
	print("image shape- ",image.shape)
	projection_matrix = np.array([      #considering this projection matrix since we don't have the actual projection
		#matrix of the available camera for now.
		[589.3667059626796, 0.0, 320.0],
		[0.0, 589.3667059626796, 240.0],
		[0.0, 0.0, 1.0]
	])
	x0=x1*z1#converting the pixel co-ordinate values into matrix substitutable values
	y0=y1*z1
	z0=z1
	inverse = np.linalg.inv(projection_matrix)
	# we follow the equation->[manipulated pixel co-ordinates matrix]=[projection_matrix]*[image co-ordinates matrix]
	# Following procedure is done to obtain the 3d image co-ordinates of the selected point for throwing projectile.
	Xc1 = inverse[0][0] * x0 + inverse[0][1] * y0 + inverse[0][2] * z0
	print(Xc1)
	Yc1 = inverse[1][0] * x0 + inverse[1][1] * y0 + inverse[1][2] * z0
	print(Yc1)
	Zc1 = inverse[2][0] * x0 + inverse[2][1] * y0 + inverse[2][2] * z0
	print(Zc1)
	#Now we may take care of the required rotation of our launch mechanism in the horizontal plane as well as in vertical plane
	#so that our launch mechanism aligns itself perfectly with the selected point of target.

	cv2.waitKey(0)
#Executing command->python detect.py --images images 
