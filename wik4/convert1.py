#color, convert image

#rgb = red gren bu
#255 255 255

#hsv = hu(tone of col) satuateion(vibrantng) value(bright)

#rgb  vd hsv
#rgb can only check 1 color
#hsv can check tone or vibant it multi
import cv2

# img = cv2.imread('C:\Users\chach\OneDrive\Desktop\superman.jpg')
img = cv2.imread('wik4\superman.jpg')


#chek red

# bit binary 0, 1
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, mask = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

result = cv2.bitwise_and(img, img, mask=mask)


cv2.imshow('Orinal', img)
cv2.imshow('Grayscale', gray)
cv2.imshow('Mask', mask)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()