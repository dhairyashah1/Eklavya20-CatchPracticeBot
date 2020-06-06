import numpy as np
import cv2

import matplotlib.pyplot as plt
from prettytable import PrettyTable
img = cv2.imread("2_(1)Orange_(2)Green.jpeg")
scan_bottom_2 = [2.5, 0.7426072359085083, 0.7522093057632446, 0.7832335829734802, 0.8059654235839844, 0.8436056971549988, 0.8713942170143127, 0.9178133606910706, 0.9524098038673401, 0.9903928637504578, 1.0548433065414429, 1.1036864519119263, 1.158162236213684, 1.2526167631149292, 1.3259865045547485, 1.4096509218215942, 1.5013911724090576, 0.5596776604652405, 0.5579584836959839, 0.5563880801200867, 0.554966151714325, 0.5536940693855286, 0.5525733828544617, 0.551605224609375, 0.5507890582084656, 0.5498579740524292, 0.5494321584701538, 0.5491631627082825, 0.5490515828132629, 0.5490549802780151, 0.549178421497345, 0.5494619607925415, 0.5499037504196167, 0.5505039095878601, 0.5512622594833374, 0.5521784424781799, 0.5532503128051758, 0.5544808506965637, 0.5558674931526184, 0.5574095845222473, 0.5600119233131409, 0.5619362592697144, 1.5080050230026245, 1.5139671564102173, 1.5203138589859009, 1.5270681381225586, 1.5379221439361572, 1.5456287860870361, 1.553727149963379, 1.5621850490570068, 1.575574278831482, 1.5849562883377075, 1.594679355621338, 1.6099306344985962, 1.620530128479004, 1.6370484828948975, 1.6484602689743042, 1.6661911010742188]
scan_top_2 = [2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0.6572976112365723, 0.6556190252304077, 0.6541200280189514, 0.6527998447418213, 0.6516598463058472, 2.5, 2.5, 2.5, 0.5414995551109314, 0.5413935780525208, 0.5413989424705505, 0.5415249466896057, 0.5418086647987366, 2.5, 2.5, 2.5, 0.6564496159553528, 0.6571106314659119, 0.6585772633552551, 0.660229504108429, 0.662063717842102, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5]

diff_scan_bottom_2 = np.diff(scan_bottom_2)
diff_scan_top_2 = np.diff(scan_top_2)
########################################################################################
for i in range(10,len(scan_bottom_2)-2):
    if -0.05<=diff_scan_bottom_2[i]<0.1  and  diff_scan_bottom_2[i+1]<=-0.1 and 0.1>=diff_scan_bottom_2[i-1]>=-0.05:
        pt1 = i

    elif diff_scan_bottom_2[i]<=0.05 and diff_scan_bottom_2[i-1]>0.1:
        pt2 = i


pt = (pt1+pt2)//2  #index of midpoint(x coordinate)
############################################################################################
tpt1 =[]
tpt2 = []
for i in range(10,len(scan_top_2)-2):
    if -0.05<=diff_scan_top_2[i]<0.1  and  diff_scan_top_2[i+1]<=-0.5 and 0.1>=diff_scan_top_2[i-1]>=-0.05:
        tpt1.append(i)

    elif diff_scan_top_2[i]<=0.05 and diff_scan_top_2[i-1]>0.1:
        tpt2.append(i)

tpt =[]
tpt.append((tpt1[0] + tpt2[0])//2)
tpt.append((tpt1[1]+ tpt2[1])//2)
tpt.append((tpt1[2] + tpt2[2])//2)
#########################################################################################
plt.figure(1)
plt.subplot(211)
plt.title('SCAN_TOP_2')
plt.plot(scan_top_2)
plt.plot(tpt[0],scan_top_2[tpt[0]],'ro')
plt.plot(tpt[1],scan_top_2[tpt[1]],'ro')
plt.plot(tpt[2],scan_top_2[tpt[2]],'ro')
plt.plot(diff_scan_top_2)
plt.grid(True)

plt.subplot(212)
plt.title('SCAN_BOTTOM_2')
plt.plot(scan_bottom_2) #by default data plotted on y axis
plt.plot(pt,scan_bottom_2[pt],'ro') #marking a point
plt.plot(diff_scan_bottom_2)
plt.grid(True)
plt.show()
##########################################################################

Zc_bot = scan_bottom_2[pt]   #Z' =Zc
Xc_bot = pt/len(scan_bottom_2)*640*Zc_bot     # pixel coordinate is Xc/Zc horizontal total pixels in image is 640
Yc_bot = 144.2 #assume at const dist depth
#BottomCameraMatrix
C_bot = np.array([ [Xc_bot],
                   [Yc_bot],
                   [Zc_bot]])
C_bot = np.matrix(C_bot)

#TopCameraMtrix
Zc_top_1=scan_top_2[tpt[0]]
Yc_top_1 = 1
Xc_top_1 = tpt[0]*640/len(scan_top_2)*Zc_top_1
C_top_1 = np.array([ [Xc_top_1],
               [Yc_top_1],
               [Zc_top_1]])
C_top_1 = np.matrix(C_top_1)

Zc_top_2 = scan_top_2[tpt[1]]
Yc_top_2 = 1
Xc_top_2 = tpt[1]*640/len(scan_top_2)*Zc_top_2
C_top_2 = np.array([ [Xc_top_2],
                     [Yc_top_2],
                     [Zc_top_2]])
C_top_2 = np.matrix(C_top_2)

Zc_top_3 = scan_top_2[tpt[1]]
Yc_top_3 = 1
Xc_top_3 = tpt[1]*640/len(scan_top_2)*Zc_top_3
C_top_3 = np.array([ [Xc_top_3],
                     [Yc_top_3],
                     [Zc_top_3]])
C_top_3 = np.matrix(C_top_3)


PROJECTION_MATRIX = np.array([[ 589.3667059626796 ,         0.0        , 320.0 ],
                              [       0.0         ,  589.3667059626796 , 240.0 ],
                              [       0.0         ,         0.0        ,  1.0  ]])
PROJECTION_MATRIX = np.matrix(PROJECTION_MATRIX)
PROJECTION_MATRIX_inv = np.linalg.inv(PROJECTION_MATRIX)

CAMERA_COORDINATE_MATRIX_bottom = PROJECTION_MATRIX_inv*C_bot
CAMERA_COORDINATE_MATRIX_top_1 = PROJECTION_MATRIX_inv*C_top_1
CAMERA_COORDINATE_MATRIX_top_2 = PROJECTION_MATRIX_inv*C_top_2
CAMERA_COORDINATE_MATRIX_top_3 = PROJECTION_MATRIX_inv*C_top_3

print("Bottom: ",CAMERA_COORDINATE_MATRIX_bottom)
print("Top_1: ",CAMERA_COORDINATE_MATRIX_top_1)
print("Top_2: ",CAMERA_COORDINATE_MATRIX_top_2)
print("Top_3: ",CAMERA_COORDINATE_MATRIX_top_3)



