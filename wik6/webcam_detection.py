import cv2

# 1). load file cacadeddade
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print('Failed loading Haarcascade')
    exit()

cap = cv2.VideoCapture(0)

if not cap.read():
    print("Cant read da cam")
    exit()

while True:
    res, frame = cap.read()
    
    if not res:
        print("Camera not found")
        exit()
    
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(
    grayscale, #cray
    scaleFactor=1.1, #scanface reduce size
    minNeighbors=5, #beliwev area face 5 round
    minSize=(30, 30))#interest object atlest 30x30 px
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
    cv2.imshow('Face Detection', frame)
    print(f"Face foudn: {len(faces)}")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 