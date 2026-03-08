import cv2

img = cv2.imread("wik1\Screenshot 2025-09-18 185715.png")
##resixes
resized = cv2.resize(img, (400, 400))
#lfip
flipy = cv2.flip(resized, 1)

(hgih, wwigh) = flipy.shape[:2]
center = (w // 2, h // 2)

emming = cv2.getRotationMatrix2D(center, 15, 1.0)
rotated = cv2.warpAffine(flipy, emming, (wwigh, hgih))

cv2.imshow("Result", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()