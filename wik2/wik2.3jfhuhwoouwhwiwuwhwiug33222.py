import cv2

img = cv2.imread("wik1\Screenshot 2025-09-18 185715.png")
#if no img
if img is None:
    print("cloud not found read the images")
    
#gay scal
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("result", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()