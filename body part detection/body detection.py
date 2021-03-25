import cv2
bd = cv2.CascadeClassifier('haarcascade_fullbody.xml')
img2 = cv2.VideoCapture('vtest.avi')#0,cv2.CAP_DSHOW)

while True:
	ret, img = img2.read()
	body = bd.detectMultiScale(gray, 1.1, 7)

	for (x1, y1, x2, y2) in body:
		cv2.rectangle(img, (x1, y1), (x1+x2, y1+y2), (0, 255, 255), 3)

	cv2.imshow('img', img)
	if cv2.waitKey(1) & 0XFF == ord('q'):
		break
img2.release()
cv2.destroyAllWindows()
