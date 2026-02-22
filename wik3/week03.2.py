#flip img
import cv2

img = cv2.imread("wik1\Screenshot 2025-09-18 185715.png")

#flip() = 1 image input 2.1 1:left right    0:(top bottom)
img_flip = cv2.flip(img,0)

cv2.imshow("flip", img_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()