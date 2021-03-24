import cv2
img = cv2.imread('WindowsLogo.jpg',1)           #image1
img2 = cv2.imread('HappyFish.jpg',1)            #image2
cv2.imshow('image', img)                        #open image1
a = cv2.waitKey(0)

if a==32:
	cv2.destroyALLWindows() 

elif a==ord('q'):
	cv2.imshow('image2',img2)              #open image2
	cv2.waitKey(0)
	cv2.destroyAllWindows()
