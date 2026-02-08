import cv2

image = cv2.imread("wik1\Screenshot 2025-09-18 185715.png")

cv2.imshow("Image for output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()