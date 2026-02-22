import cv2 #call module
#define a variable image keep value call module cv2 func
#imread is reading an image and in func
image = cv2.imread("wik1\Screenshot 2025-09-18 185715.png")
#inshow is dhow iamge define with 2 parameter = labwl imagef
cv2.imshow("Image for output", image)
#wait for program until someone typew
cv2.waitKey(0)
#close program
cv2.destroyAllWindows()