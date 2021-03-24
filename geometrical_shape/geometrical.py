import numpy as np
import cv2
img = cv2.imread('WindowsLogo.jpg',1)

img = cv2.line(img, (100, 0), (100,230), (0, 255, 0), 3)
img = cv2.arrowedLine(img, (0, 130), (255,130), (100, 0, 0), 3)

img = cv2.rectangle(img, (0, 0), (300,200), (0, 0, 250), 3)
img = cv2.rectangle(img, (40, 40), (80,70), (0, 0, 250), -1)

img = cv2.circle(img, (255, 100), 50, (0, 250, 250), 3)
img = cv2.circle(img, (260, 130), 10, (250, 0, 250), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'VORDY', (30,120), font, 1, (100, 10, 10), 3)

# img = np.zeros((250, 350, 3), np.uint8)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()