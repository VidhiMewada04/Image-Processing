import cv2
import easyocr as ocr
from matplotlib import pyplot as plt
import numpy as np 

reader = ocr.Reader(['en'], gpu = False)

for x in range(1, 5):
	result = reader.readtext(f'{x}.jpg')
	print(result[0][1])

	tl = tuple(result[0][0][0])
	br = tuple(result[0][0][2])
	text = result[0][1]
	font = cv2.FONT_HERSHEY_SIMPLEX

	img = cv2.imread(f'{x}.jpg')
	img = cv2.rectangle(img, tl, br, (0,255,0), 5)
	img = cv2.putText(img, text, tl, font, 1.5, (255, 0, 0), 5, cv2.LINE_AA)
	plt.imshow(img)
	plt.show()

#####################################################################################################3

# import cv2
# import easyocr as ocr
# import imutils 
# from matplotlib import pyplot as plt
# import numpy as np

# img = cv2.imread("img.jpeg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # filt = cv2.bilateralFilter(gray, 11, 17, 17)
# edge = cv2.Canny(gray, 30, 200) 
# point = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contours = imutils.grab_contours(point)
# contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# location = None
# for contour in contours:
# 	approx = cv2.approxPolyDP(contour, 10, True)
# 	if len(approx) == 4:
# 		location = approx
# 		break
# print(location)

# mask = np.zeros(gray.shape, np.uint8)
# new_img = cv2.drawContours(mask, [location], 0, 255, -1)
# new_img = cv2.bitwise_and(img, img, mask=mask)

# # plt.imshow(gray)
# plt.imshow(new_img)
# # plt.imshow(cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB))
# plt.show()
# # cv2.waitKey(1000)