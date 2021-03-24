import cv2
cap = cv2.VideoCapture('tree.avi',1)

while True:
	ret, frame = cap.read()

	if ret == True:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		cv2.imshow('frame', frame)      #will run cap
		cv2.imshow('gray', gray)        #will run cap in gray mode
		if cv2.waitKey(1) & 0XFF == ord('q'):
			break                   #to exit frame press "q"
	else:
		break
cap.release()
cv2.destroyAllWindows()

###############################################################################################3
#/*************if you want to open camera*****************/

# import cv2
# cap = cv2.VideoCapture(0)   #or  cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# while(True):
# 	_, frame = cap.read()
# 	cv2.imshow('frame', frame)
# 	if cv2.waitKey(30) & 0XFF == ord('q'):
#  		break

# cap.release()
# cv2.destroyAllWindows()
