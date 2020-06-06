import numpy as np
import cv2

import matplotlib.pyplot as plt
from prettytable import PrettyTable

scan_bottom_3 = [2.5, 1.4491560459136963, 1.4521547555923462, 1.4617453813552856, 1.468658685684204, 1.4798585176467896, 1.4879097938537598, 1.5009211301803589, 1.5102533102035522, 1.5201414823532104, 1.5360751152038574, 1.547473430633545, 1.246402382850647, 1.2116153240203857, 1.1786918640136719, 1.1475194692611694, 1.1038010120391846, 1.100621223449707, 1.1123900413513184, 1.1247979402542114, 1.137876272201538, 1.1516659259796143, 1.1661937236785889, 1.1814883947372437, 1.1975963115692139, 1.2145583629608154, 1.8587009906768799, 1.8875850439071655, 1.9179909229278564, 1.9666296243667603, 1.98369300365448, 2.0191638469696045, 2.0295772552490234, 1.9995408058166504, 1.219978928565979, 1.2031865119934082, 1.1872395277023315, 1.172090768814087, 1.1576956510543823, 1.1374597549438477, 1.1248279809951782, 1.1128361225128174, 1.1014621257781982, 1.1137665510177612, 1.1440902948379517, 1.176161527633667, 1.2278165817260742, 1.2648286819458008, 1.6815615892410278, 1.6635421514511108, 1.652355432510376, 1.6418139934539795, 1.6271061897277832, 1.618003487586975, 1.6053541898727417, 1.5975602865219116, 1.5867301225662231, 1.5800886154174805]
scan_top_3 = [2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 1.2118160724639893, 1.1788828372955322, 1.179290771484375, 1.190598964691162, 1.318230390548706, 2.5, 1.184429407119751, 1.1575344800949097, 1.1507326364517212, 1.1652424335479736, 1.2978417873382568, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 1.3028520345687866, 1.1722204685211182, 1.157829761505127, 1.1526159048080444, 2.5, 2.5, 1.315839409828186, 1.1968878507614136, 1.1856797933578491, 1.1802948713302612, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5]

diff_scan_bottom_3 = np.diff(scan_bottom_3)
diff_scan_top_3 = np.diff(scan_top_3)

#lists of indexes
pt1=[]
pt2=[]
pt=[]
######################################################################################
for i in range(10,len(scan_bottom_3)-2):
    if -0.05<=diff_scan_bottom_3[i]<0.1  and  diff_scan_bottom_3[i+1]<=-0.1 and 0.1>=diff_scan_bottom_3[i-1]>=-0.05:
        pt1.append(i)

    elif diff_scan_bottom_3[i]<=0.05 and diff_scan_bottom_3[i-1]>0.1:
        pt2.append(i)

pt.append((pt1[0]+pt2[0])//2)  #index of midpoint(x coordinate)
pt.append((pt1[1]+pt2[1])//2)

####################################################################################
tpt1 =[]    # 4 points
tpt2 = []
for i in range(0,len(scan_top_3)-2):
    if -1.5<=diff_scan_top_3[i]<1.5  and  diff_scan_top_3[i+1]<=-0.18 and diff_scan_top_3[i-1]>=-0.05:
        tpt1.append(i)

    if diff_scan_top_3[i]<=0.05 and diff_scan_top_3[i-1]>0.1:
        tpt2.append(i)
#print(tpt1)
#print(tpt2)
tpt =[]
tpt.append((tpt1[0] + tpt2[0])//2)
tpt.append((tpt1[1]+ tpt2[1])//2)
tpt.append((tpt1[2] + tpt2[2])//2)
tpt.append((tpt1[3] + tpt2[3])//2)
##################################################################################
#plt.figure(1)
plt.subplot(211)
plt.title("SCAN_TOP_3")
plt.plot(scan_top_3)
plt.plot(tpt[0],scan_top_3[tpt[0]],'ro')
plt.plot(tpt[1],scan_top_3[tpt[1]],'ro')
plt.plot(tpt[2],scan_top_3[tpt[2]],'ro')
plt.plot(tpt[3],scan_top_3[tpt[3]],'ro')
plt.plot(diff_scan_top_3)
plt.grid(True)

plt.subplot(212)
plt.title("SCAN_BOTTOM_3")
plt.plot(scan_bottom_3) #by default its y axis
plt.plot(pt[0],scan_bottom_3[pt[0]],'ro')
plt.plot(pt[1],scan_bottom_3[pt[1]],'ro')
plt.plot(diff_scan_bottom_3)
plt.grid(True)
plt.show()

####################################################################################
Zc_bot_1 = scan_bottom_3[pt[0]]   #Z' =Zc
Xc_bot_1 = pt[0]/len(scan_bottom_3)*640*Zc_bot_1     # pixel coordinate is Xc/Zc horizontal total pixels in image is 640
Yc_bot_1 = 279.37 #assume at const dist depth
#BottomCameraMatrix1
C_bot_1 = np.array([ [Xc_bot_1],
                   [Yc_bot_1],
                   [Zc_bot_1]])
C_bot_1= np.matrix(C_bot_1)

Zc_bot_2 = scan_bottom_3[pt[1]]   #Z' =Zc
Xc_bot_2 = pt[1]/len(scan_bottom_3)*640*Zc_bot_2    # pixel coordinate is Xc/Zc horizontal total pixels in image is 640
Yc_bot_2 = 282.37 #assume at const dist depth
#BottomCameraMatrix2
C_bot_2 = np.array([ [Xc_bot_2],
                   [Yc_bot_2],
                   [Zc_bot_2]])
C_bot_2= np.matrix(C_bot_2)

#TopCameraMatrix
Zc_top_1=scan_top_3[tpt[0]]
Yc_top_1 = 1
Xc_top_1 = tpt[0]*640/len(scan_top_3)*Zc_top_1
C_top_1 = np.array([ [Xc_top_1],
               [Yc_top_1],
               [Zc_top_1]])
C_top_1 = np.matrix(C_top_1)

Zc_top_2 = scan_top_3[tpt[1]]
Yc_top_2 = 1
Xc_top_2 = tpt[1]*640/len(scan_top_3)*Zc_top_2
C_top_2 = np.array([ [Xc_top_2],
                     [Yc_top_2],
                     [Zc_top_2]])
C_top_2 = np.matrix(C_top_2)

Zc_top_3 = scan_top_3[tpt[2]]
Yc_top_3 = 1
Xc_top_3 = tpt[2]*640/len(scan_top_3)*Zc_top_3
C_top_3 = np.array([ [Xc_top_3],
                     [Yc_top_3],
                     [Zc_top_3]])
C_top_3 = np.matrix(C_top_3)

Zc_top_4 = scan_top_3[tpt[3]]
Yc_top_4 = 1
Xc_top_4 = tpt[2]*640/len(scan_top_3)*Zc_top_4
C_top_4 = np.array([ [Xc_top_4],
                     [Yc_top_4],
                     [Zc_top_4]])
C_top_4 = np.matrix(C_top_4)

############################################################################################
PROJECTION_MATRIX = np.array([[ 589.3667059626796 ,         0.0        , 320.0 ],
                              [       0.0         ,  589.3667059626796 , 240.0 ],
                              [       0.0         ,         0.0        ,  1.0  ]])
PROJECTION_MATRIX = np.matrix(PROJECTION_MATRIX)
PROJECTION_MATRIX_inv = np.linalg.inv(PROJECTION_MATRIX)

CAMERA_COORDINATE_MATRIX_bottom_1 = PROJECTION_MATRIX_inv*C_bot_1
CAMERA_COORDINATE_MATRIX_bottom_2 = PROJECTION_MATRIX_inv*C_bot_2
CAMERA_COORDINATE_MATRIX_top_1 = PROJECTION_MATRIX_inv*C_top_1
CAMERA_COORDINATE_MATRIX_top_2 = PROJECTION_MATRIX_inv*C_top_2
CAMERA_COORDINATE_MATRIX_top_3 = PROJECTION_MATRIX_inv*C_top_3
CAMERA_COORDINATE_MATRIX_top_4 = PROJECTION_MATRIX_inv*C_top_4

print("Bottom_1: ",CAMERA_COORDINATE_MATRIX_bottom_1)
print("Bottom_2: ",CAMERA_COORDINATE_MATRIX_bottom_2)
print("Top_1: ",CAMERA_COORDINATE_MATRIX_top_1)
print("Top_2: ",CAMERA_COORDINATE_MATRIX_top_2)
print("Top_3: ",CAMERA_COORDINATE_MATRIX_top_3)
print("Top_4: ",CAMERA_COORDINATE_MATRIX_top_4)
