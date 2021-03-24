import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread("pic1.png",0)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize= 5)             #kernel size should be odd and >31
lap = np.uint8(np.absolute(lap))

sobelx = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelx = np.uint8(np.absolute(sobelx))
sobely = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = np.uint8(np.absolute(sobely))
sobel = cv2.bitwise_or(sobelx, sobely)

canny = cv2.Canny(img, 100, 100)
ret,th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('canny', canny)2
plt.show()
cv2.waitKey(0)
cv2.destroyALLWindow()
