import cv2
import numpy as np 

img = cv2.VideoCapture('vtest.avi')
background = cv2.createBackgroundSubtractorMOG2()

while(1):
	ret, cap = img.read()
	mask = background.apply(cap)

	cv2.imshow('cap', cap)
	cv2.imshow('mask', mask)

	if cv2.waitKey(1) & 0XFF == ord('q'):
		break

img.release()
cv2.destroyAllWindows() 
