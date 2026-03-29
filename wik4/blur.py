import cv2

img = cv2.imread('wik4\superman.jpg')

blurred = cv2.GaussianBlur(img, (5, 5), 0)

edges = cv2.Canny(blurred, 10, 150)

cv2.imshow('Blurred', blurred)
cv2.imshow('Edges', edges)
cv2.waitKey(0)