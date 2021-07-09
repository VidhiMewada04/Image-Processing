# import cv2
# import deepface as df#import DeepFace as df
# fc = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0)

# while True:
# 	ret,frame = cap.read()
# 	result = df.analyze(frame, actions = ['emotions'])

##################################################################################3

import cv2
import numpy as np
import matplotlib.pyplot as plt
import deepface.DeepFace as df
fc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread("1.jpeg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = fc.detectMultiScale(img, 1.1, 4)

for (x1, y1, x2, y2) in face:
	cv2.rectangle(img, (x1, y1), (x1+x2, y1+y2), (0, 255, 255), 3)

predictions = df.analyze(img)
print(predictions['dominant_emotion'])
# print(predictions)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

#################################################################

# for x in range (1, 6):
# 	img = cv2.imread(f'{x}.jpeg')[:,:,0]
# 	# gray = cv2.cvtColor(cv2.UMat(img), cv2.COLOR_BGR2GRAY)
# 	# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 	face = fc.detectMultiScale(img, 1.1, 4)

# 	for (x1, y1, x2, y2) in face:
# 		cv2.rectangle(cv2.UMat(img), (x1, y1), (x1+x2, y1+y2), (0, 255, 255), 3)

# 	predictions = df.analyze(img)
# 	print(predictions['dominant_emotion'])

# 	plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# 	plt.show()