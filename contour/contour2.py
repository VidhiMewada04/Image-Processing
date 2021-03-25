
import numpy as np
import cv2

vid = cv2.VideoCapture('vtest.avi')

while True:
	ret, cap = vid.read()
	cv2.imshow('vid',cap);
	if ret == True:
		gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
		blur = cv2.GaussianBlur(gray,(5,5),0)
		_, thresh = cv2.threshold(blur, 127, 255, 1)
		th = thresh.copy()
		contours, _= cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		for contour in contours:
			cv2.drawContours(th, contours, -1, (0, 255, 255), 3)
			cv2.drawContours(cap, contours, -1, (0, 255, 255), 3)
		cv2.rectangle(cap, (300, 100), (500,200), (0, 0, 250), 3)
		cv2.imshow('cap', cap)
		cv2.rectangle(th, (300, 100), (500,200), (0, 0, 250), 3)
		cv2.imshow('th', th)
		
	if cv2.waitKey(30) & 0XFF == ord('q'):
		break

vid.release()
cv2.waitKey(0)
cv2.destroyAllWindows()


