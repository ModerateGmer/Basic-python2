#rotate
import cv2

img = cv2.imread("wik1\Screenshot 2025-09-18 185715.png")

#find a center an image height /2 width/2
height, width = img.shape[:2]
center = (width // 2, height // 2)

#getrotmat2d 1 center 2 deg 3 scale
matrix = cv2.getRotationMatrix2D(center, 45 ,1.0)

img_rotated = cv2.warpAffine(img, matrix,(width, height))

cv2.imshow("Rotated", img_rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()