import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread("baboon.jpg")

gp = [img]                      #gaussian pyramid
for i in range(6):
	img = cv2.pyrDown(img)
	gp.append(img)
	cv2.imshow(str(i),img)
img = gp[5]
cv2.imshow('gpimg',img)

lp = [img]                      #laplacian pyramid 
for i in range(5, 0, -1):
	ext = cv2.pyrUp(gp[i])
	lap = cv2.subtract(gp[i-1],ext)
	lp.append(lap)
	cv2.imshow(str(i),lap)
img = lp[5]
cv2.imshow('lpimg',img)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
