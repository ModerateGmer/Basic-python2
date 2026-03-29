import cv2
#0 is -camera tggle
cap = cv2.VideoCapture(0)
img = cv2.imread('wik5\images (2).jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
if not cap.read():
    print("cant open cam")
cv2.imshow('Grayscale', gray)
while True:
    res,frame = cap.read()
#if no capread = cant open cam
    if not res:
        print("cannot recieve frame exiting...................................")
        break
    cv2.imshow("mycam", frame)
    
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
            