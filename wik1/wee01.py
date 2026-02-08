import cv2

image = cv2.imread("wik1\Screenshot 2025-09-18 185715.png")

#save img


save_image = cv2.imwrite("new2.png", image)
#read new file image
newFile = cv2.imread("new2.png")
cv2.imshow("test", newFile)
cv2.waitKey(0)
cv2.destroyAllWindows()