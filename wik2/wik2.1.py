import cv2
#0 is -camera tggle
cap = cv2.VideoCapture(0)

if not cap.read():
    print("cant open cam")
    
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
            