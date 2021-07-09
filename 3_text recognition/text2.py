import cv2
import easyocr as ocr
# from matplotlib import pyplot as plt
# import numpy as np

reader = ocr.Reader(['en'], gpu = False)
video = cv2.VideoCapture(0)

while True:
	ret, frame = video.read()
	result = reader.readtext(frame)
	print(result)
	# print(result[0][1])

	# tl = tuple(result[0][0][0])
	# br = tuple(result[0][0][2])
	# frame = cv2.rectangle(frame, tl, br, (0,255,0), 5)

	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

###############################################################################

# import cv2
# import easyocr as ocr
# import imutils 
# from matplotlib import pyplot as plt
# import numpy as np

# video = cv2.VideoCapture(0)

# while True:
# 	ret, img = video.read()
# 	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# 	edge = cv2.Canny(gray, 30, 200) 
# 	point = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 	contours = imutils.grab_contours(point)
# 	contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# 	location = None
# 	for contour in contours:
# 		approx = cv2.approxPolyDP(contour, 10, True)
# 		if len(approx) == 4:
# 			location = approx
# 			break
# 	print(location)

# 	mask = np.zeros(gray.shape, np.uint8)
# 	new_img = cv2.drawContours(mask, [location], 0, 255, -1)
# 	new_img = cv2.bitwise_and(img, img, mask=mask)

# 	cv2.imshow('new', new_img)
# 	# plt.imshow(cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB))
# 	# plt.show()
	
# 	if cv2.waitKey(1) & 0xFF == ord("q"):
# 		break

# video.release()
# cv2.destroyAllWindows()