import numpy as np
import cv2

img = cv2.imread('line1.jpg')
cv2.imshow('img', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for c in contours:
	cv2.drawContours(gray, contours, -1, (0, 255, 0), 3)
	cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
	cap = cv2.contourArea(c)
	# print(cap) 
	if cv2.contourArea(c) > 13000 : 
		cv2.imshow('img_contour', img)
		cv2.imshow('gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


##########################################################################

import cv2    
img=cv2.imread('line1.jpg') 

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

ret,thresh=cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)

countours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(img,countours,-1, (0,255,0), -1)
cv2.imshow("Contour",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
