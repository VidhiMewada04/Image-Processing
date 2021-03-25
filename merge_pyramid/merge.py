import cv2
import numpy as np
from matplotlib import pyplot as plt 

img1 = cv2.imread("apple.jpg")
img2 = cv2.imread("orange.jpg")
a_o = np.hstack( (img1[:, :256], img2[:, 256:]) )
cv2.imshow("apple.jpg",img1)
cv2.imshow("orange.jpg",img2)
cv2.imshow("apple&orange",a_o)

apple = img1.copy()
gp1 = [apple]                      
for i in range(6):
	apple = cv2.pyrDown(apple)
	gp1.append(apple)
	# cv2.imshow(str(i),apple)

orange = img2.copy()
gp2 = [orange]                
for i in range(6):
	orange = cv2.pyrDown(orange)
	gp2.append(orange)
	# cv2.imshow(str(i),orange)

apple = gp1[5]
lp1 = [apple]                    
for i in range(5, 0, -1):
	ext = cv2.pyrUp(gp1[i])
	lap = cv2.subtract(gp1[i-1],ext)
	lp1.append(lap)
	# cv2.imshow(str(i),lap)

orange = gp2[5]
lp2 = [orange]                      
for i in range(5, 0, -1):
	ext = cv2.pyrUp(gp2[i])
	lap = cv2.subtract(gp2[i-1],ext)
	lp2.append(lap)
	# cv2.imshow(str(i),lap)

pyramid = []
for lap1, lap2 in zip(lp1, lp2):
	cols, rows, ch = lap1.shape
	laplacian = np.hstack( (lap1[:, :int(cols/2)], lap2[:, int(cols/2):]) )
	pyramid.append(laplacian)

reconstruct = pyramid[0]
for i in range (1, 6):
	reconstruct = cv2.pyrUp(reconstruct)
	reconstruct = cv2.add(pyramid[i], reconstruct)

cv2.imshow('reconstruct',reconstruct)

cv2.waitKey(0)
cv2.destroyllWindows()
