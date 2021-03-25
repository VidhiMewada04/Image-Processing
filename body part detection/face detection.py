import cv2
fc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture('video.avi')#0,cv2.CAP_DSHOW)

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	face = fc.detectMultiScale(gray, 1.1, 4)

	for (x1, y1, x2, y2) in face:
		cv2.rectangle(img, (x1, y1), (x1+x2, y1+y2), (0, 255, 255), 3)
	cv2.imshow('img', img)
	if cv2.waitKey(1) & 0XFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
