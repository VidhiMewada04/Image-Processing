import numpy as np 
import cv2

img1 = cv2.imread('baboon.jpg')
img2 = cv2.imread('HappyFish.jpg')

print(img1.shape)
print(img1.size)
print(img1.dtype)

b, g, r = cv2.split(img1)                    # to change colour               
img1 = cv2.merge((b, g, r))

crop1 = img1[20:100, 110:400]               # cropped img   
crop2 = img1[105:185, 110:400]              # [y1:y2, x1:x2]
cv2.imshow('crop1', crop1) 
cv2.imshow('crop2', crop2) 

eye = img1[20:100, 110:400]                  # coppied img
img1[105:185, 110:400] = eye
cv2.imshow('image1', img1)

img1 = cv2.resize(img1, (512, 512))           # merge img
img2 = cv2.resize(img2, (512, 512))
dst = cv2.addWeighted(img1, .7, img2, .3, 0)       #(first img, fade of img1, second img, fade of img2)
cv2.imshow('dst', dst)


cv2.waitKey(0)
cv2.destroyAllWindows()
