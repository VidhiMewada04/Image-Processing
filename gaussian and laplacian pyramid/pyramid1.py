import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread("baboon.jpg")

pyr = cv2.pyrDown(img)
pyr2 = cv2.pyrUp(pyr)
cv2.imshow("pyr",pyr)
cv2.imshow("pyr2",pyr2)

cv2.waitKey(0)
cv2.destroyAllWindows()
