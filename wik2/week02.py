import cv2

cap = cv2.VideoCapture("video\meme2.mp4")
#isopened is it read id it reading video
while cap.isOpened():
    #res and fram is  capread
    res, frame = cap.read()
    #if no cap read
    if not res:
        print("VIDEO not found")
        break
    
    cv2.imshow("Output", frame)
    #1 mean customizse press butrontw q 4 out

    if cv2.waitKey(1) == ord('q'):
        break
#waitkewy 0 s means press anybutton4
#it meen show ooppooo the im cap 4m vdo
cap.release()
cv2.destroyAllWindows()
