#plot of data(distance from lidar)(PLOT: y axis)::Z coordinate in image pixel system vs no of elements(PLOT:x-axis)
import numpy as np
import cv2

img = cv2.imread('1_(1)Yellow_(2)Blue.jpeg')
import matplotlib.pyplot as plt
from prettytable import PrettyTable

scan_bottom_1 = [2.5, 1.0008981227874756, 0.9995380640029907, 1.0943686962127686, 1.1830064058303833, 1.4564176797866821, 1.4524344205856323, 1.450128197669983, 1.4481055736541748, 1.4456132650375366, 1.444341778755188, 1.443387508392334, 1.4425603151321411, 1.442441463470459, 1.4425129890441895, 1.4429126977920532, 1.4436900615692139, 1.4455636739730835, 1.4472864866256714, 1.4494212865829468, 1.4519659280776978, 1.4549174308776855, 1.4583097696304321, 0.8760384321212769, 0.7989348769187927, 0.7057613730430603, 0.6549088954925537, 0.6529011726379395, 0.6557028293609619, 0.658721923828125, 0.6619646549224854, 0.665429413318634, 0.6691219210624695, 0.6730482578277588, 0.67720627784729, 0.6816044449806213, 0.6862402558326721, 0.6911192536354065, 0.6962470412254333, 0.7016206383705139, 0.7101544141769409, 0.7161607146263123, 0.7224243879318237, 0.7289506793022156, 0.7357357144355774, 1.359674096107483, 1.326892614364624, 1.2962515354156494, 1.2675635814666748, 1.2278528213500977, 1.2033909559249878, 1.1803871393203735, 1.1484110355377197, 1.1286132335662842, 1.1010079383850098, 1.0838795900344849, 1.0599266290664673, 1.0450222492218018]
scan_top_1 = [2.5, 1.0938091278076172, 1.0894696712493896, 1.1207243204116821, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0.7562490701675415, 0.7435263395309448, 0.746489405632019, 0.749693751335144, 0.753146767616272, 0.8518658876419067, 0.8563241362571716, 0.8610755205154419, 0.7037549614906311, 0.6792469620704651, 0.6814751625061035, 0.6861121654510498, 0.6909923553466797, 0.6961185336112976, 0.8021950721740723, 0.8119485974311829, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5]

#derivative function
diff_scan_bottom_1 = np.diff(scan_bottom_1)
diff_scan_top_1 = np.diff(scan_top_1)
#########################################################################################
for i in range(20,len(scan_bottom_1)-2):
    if -0.05<=diff_scan_bottom_1[i]<0.1  and  diff_scan_bottom_1[i+1]<=-0.1 and 0.1>=diff_scan_bottom_1[i-1]>=-0.05:
        pt1 = i

    elif diff_scan_bottom_1[i]<=0.05 and diff_scan_bottom_1[i-1]>0.1:
        pt2 = i
#print(pt1 , pt2)
pt = (pt1+pt2)//2  #index of midpoint(PLOT:x axis coordinate)(Image pixel: Z coordinate)
#print(scan_bottom_1[pt]) #actually its the z coordinate of camera coordinate sysytem

#############################################################################################
tpt1 = []
tpt2 = []
for i in range(10,len(scan_top_1)-2):
    if -0.05<=diff_scan_top_1[i]<0.1  and  diff_scan_top_1[i+1]<=-0.1 and 0.1>=diff_scan_top_1[i-1]>=-0.05:
        tpt1.append(i)

    elif diff_scan_top_1[i]<=0.05 and diff_scan_top_1[i-1]>0.08:
        tpt2.append(i)

tpt =[]
tpt.append((tpt1[0] + tpt2[0])//2)
tpt.append((tpt1[1] + tpt2[1])//2)

################################################################################################
plt.figure(1)
plt.subplot(211)
plt.title('SCAN_TOP_1')
plt.plot(scan_top_1)
plt.plot(tpt[0],scan_top_1[tpt[0]],'ro')
plt.plot(tpt[1],scan_top_1[tpt[1]],'ro')
plt.plot(diff_scan_top_1)
plt.grid(True)

plt.subplot(212)
plt.title('SCAN_BOTTOM_1')
plt.plot(scan_bottom_1) #by default data plotted on y axis
plt.plot(pt,scan_bottom_1[pt],'ro') #marking a point
plt.plot(diff_scan_bottom_1)
plt.grid(True)
plt.show()
#######################################################################################
#we get pixel coordinates first
Zc_bot = scan_bottom_1[pt]   #Z' =Zc
Xc_bot = pt/len(scan_bottom_1)*640*Zc_bot     # pixel coordinate is Xc/Zc horizontal total pixels in image is 640
Yc_bot = 174  #assume at const dist depth
#BottomCameraMatrix
C_bot = np.array([ [Xc_bot],
               [Yc_bot],
               [Zc_bot]])
C_bot = np.matrix(C_bot)

#TopCameraMtrix
Zc_top_1=scan_top_1[tpt[0]]
Yc_top_1 = 1
Xc_top_1 = tpt[0]*640/len(scan_top_1)*Zc_top_1
C_top_1 = np.array([ [Xc_top_1],
               [Yc_top_1],
               [Zc_top_1]])
C_top_1 = np.matrix(C_top_1)

Zc_top_2 = scan_top_1[tpt[1]]
Yc_top_2 = 1
Xc_top_2 = tpt[1]*640/len(scan_top_1)*Zc_top_2
C_top_2 = np.array([ [Xc_top_2],
               [Yc_top_2],
               [Zc_top_2]])
C_top_2 = np.matrix(C_top_2)


PROJECTION_MATRIX = np.array([[ 589.3667059626796 ,         0.0        , 320.0 ],
                              [       0.0         ,  589.3667059626796 , 240.0 ],
                              [       0.0         ,         0.0        ,  1.0  ]])
PROJECTION_MATRIX = np.matrix(PROJECTION_MATRIX)
PROJECTION_MATRIX_inv = np.linalg.inv(PROJECTION_MATRIX)

CAMERA_COORDINATE_MATRIX_bottom = PROJECTION_MATRIX_inv*C_bot
CAMERA_COORDINATE_MATRIX_top_1 = PROJECTION_MATRIX_inv*C_top_1
CAMERA_COORDINATE_MATRIX_top_2 = PROJECTION_MATRIX_inv*C_top_2

print("Bottom: ",CAMERA_COORDINATE_MATRIX_bottom)
print("Top_1: ",CAMERA_COORDINATE_MATRIX_top_1)
print("Top_2: ",CAMERA_COORDINATE_MATRIX_top_2)

