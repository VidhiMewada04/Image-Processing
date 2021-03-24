import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

img = cv2.imread('HappyFish.jpg')
img = mpimg.imread("HappyFish.jpg")
cv2.imshow('img',img)

plt.axis("off")
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
