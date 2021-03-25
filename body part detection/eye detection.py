import cv2
ey = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture('video.avi')#0,cv2.CAP_DSHOW)

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	eye = ey.detectMultiScale(gray, 1.1, 4)

	for (x1, y1, x2, y2) in eye:
		cv2.rectangle(img, (a, b), (a+c, b+d), (0, 255, 255), 3)
	cv2.imshow('img', img)
	if cv2.waitKey(1) & 0XFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
