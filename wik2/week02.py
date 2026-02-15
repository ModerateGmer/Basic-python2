import cv2

cap = cv2.VideoCapture("video\meme2.mp4")

while cap.isOpened():
    res, frame = cap.read()
    
    if not res:
        print("VIDEO not found")
        break
    
    cv2.imshow("Output", frame)
    #1 mean customizse press butrontw q 4 out

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()


cv2.destroyAllWindows()
