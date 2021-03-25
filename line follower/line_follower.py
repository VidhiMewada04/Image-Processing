import numpy as np
import cv2

img = cv2.VideoCapture('video6.avi')
	
while True:
	ret, cap = img.read()	
	# print(cap.shape)

	gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	_, th = cv2.threshold(blur, 127, 255, 0 )
	contours, _= cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	# counter = 0
	for contour in range(len(contours)):
		area = cv2.contourArea(contours[contour])
		# print(area)
		x1,y1,x2,y2 = cv2.boundingRect(contours[contour])

		if area > 20000 and y2 > 479:
			center = x1+(x2/2)
			print(center)
			if (400 < center < 448): 
				cv2.drawContours(cap, contours[contour], -1, (0, 255, 0), 10)
				print("forward")
			elif (10 < center < 400):
				cv2.drawContours(cap, contours[contour], -1, (255, 0, 0), 10)
				print("right")
			elif (448 < center < 848):
				cv2.drawContours(cap, contours[contour], -1, (0, 0, 255), 10)
				print("left")
	cv2.imshow('cap', cap)
	if cv2.waitKey(1) & 0XFF == ord('q'):
		break

img.release()
cv2.destroyAllWindows()
