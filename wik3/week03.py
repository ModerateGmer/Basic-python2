import cv2
#resize

img = cv2.imread("wik1\Screenshot 2025-09-18 185715.png")
img_resize = cv2.resize(img,(300,450));


cv2.imshow('Resized', img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()