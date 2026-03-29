import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('wik4\superman.jpg')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayscale_3inch = cv2.cvtColor(grayscale, cv2.COLOR_GRAY2RGB)

img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([0 , 120 , 70])
upper_red = np.array([10 , 255 , 255])

mask = cv2.inRange(img_hsv, lower_red, upper_red)

color_part = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)

grayscale_part = cv2.bitwise_and(grayscale_3inch, grayscale_3inch, mask=cv2.bitwise_not(mask))

fianl_iamge = cv2.add(color_part, grayscale_part)

cv2.imshow('RGB',img_rgb)
cv2.imshow('GrayScale',grayscale)
cv2.imshow('3inch',grayscale_3inch)
cv2.imshow('HSV',img_hsv)
cv2.imshow('COLOR Part',color_part)
cv2.imshow('GrayScale Part', grayscale_part)

plt.imshow(fianl_iamge)
plt.title('Color splash: RED ONLY!')
plt.show()