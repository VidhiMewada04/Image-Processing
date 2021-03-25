import cv2
sm = cv2.CascadeClassifier('haarcascade_smile.xml')
img2 = cv2.VideoCapture('video.avi')#0,cv2.CAP_DSHOW)

while True:
	ret, img = img2.read()
	smile = sm.detectMultiScale(gray, 1.5, 50)

	for (x1, y1, x2, y2) in smile:
		cv2.rectangle(img, (p, q), (p+r, q+s), (0, 255, 255), 2)


	cv2.imshow('img', img)
	if cv2.waitKey(1) & 0XFF == ord('q'):
		break
img2.release()
cv2.destroyAllWindows()
