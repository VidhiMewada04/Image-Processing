import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')
ret, cap1 = cap.read()
ret, cap2 = cap.read()
cap3 = 0

while True:
	diff = cv2.absdiff(cap1, cap2)
	gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (1, 1), 0)
	ret, thresh = cv2.threshold(blur, 100, 255, 0)
	dilate = cv2.dilate(thresh, None, 3)
	contours, hierarchy = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for c in contours:
		(x1, y1, x2, y2) = cv2.boundingRect(c)
		if cv2.contourArea(c) > 700 : 
			cap3 = cap1
		cv2.rectangle(cap1, (x1, y1), (x1+x2, y1+y2), (0, 255, 255), 3)
	cv2.imshow('cap3', cap3)
	cap1 = cap2
	ret, cap2 = cap.read()
	if cv2.waitKey(30) & 0XFF == ord('q'):
		break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

