import cv2
import numpy as numpy
# from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png', 0)

ret,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret,th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret,th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret,th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret,th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
th6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 2)
th7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 2)

cv2.imshow('img',img)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)
cv2.imshow('th4',th4)
cv2.imshow('th5',th5)
cv2.imshow('th6',th6)
cv2.imshow('th7',th7)

cv2.waitKey(0)
cv2.destroyAllWindows()
