# to run code on photo

import cv2
import numpy as np

def nothing(x):
	pass

cv2.namedWindow('Tracking')

cv2.createTrackbar('LH','Tracking', 0, 255, nothing)
cv2.createTrackbar('LS','Tracking', 0, 255, nothing)
cv2.createTrackbar('LV','Tracking', 0, 255, nothing)

cv2.createTrackbar('UH','Tracking', 255, 255, nothing)
cv2.createTrackbar('US','Tracking', 255, 255, nothing)
cv2.createTrackbar('UV','Tracking', 255, 255, nothing)

while True:
	frame = cv2.imread('smarties.png')
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lh = cv2.getTrackbarPos('LH', 'Tracking')
	ls = cv2.getTrackbarPos('LS', 'Tracking')
	lv = cv2.getTrackbarPos('LV', 'Tracking')

	uh = cv2.getTrackbarPos('UH', 'Tracking')
	us = cv2.getTrackbarPos('US', 'Tracking')
	uv = cv2.getTrackbarPos('UV', 'Tracking')

	lb = np.array([lh, ls, lv])
	ub = np.array([uh, us, uv])

	mask = cv2.inRange(hsv, lb, ub)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res',res)

	if cv2.waitKey(1) & 0XFF == ord('q'):
		break
		
cv2.destroyAllWindows()

######################################################################

# to run code on video

# import cv2 
# import numpy as np  
  
# cap = cv2.VideoCapture('vtest.avi')  
 

# while(1):        
#     ret, frame = cap.read() 

#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     lower_y = np.array([20, 100, 100]) 
#     upper_y = np.array([30, 255, 255]) 
#     mask = cv2.inRange(hsv, lower_y, upper_y)
#     res = cv2.bitwise_and(frame,frame, mask= mask)
#     cv2.imshow('frame',frame)
#     cv2.imshow('mask',mask)
#     if cv2.waitKey(20) & 0XFF == ord('q'):
#     	break
# cap.release()  
# cv2.destroyAllWindows()

