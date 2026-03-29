#use grayscale cuz it uses less time also this use har casevcbadce
import cv2

#load har
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print('Failed loading Haarcascade')
    exit()

#load igm
img = cv2.imread('wik5\images (11).jpg')

if img is None:
    print('image not found')
    exit()
#conv to bw
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    

#afce detect
#detectmulsca = dect obj
#if obj near => big face
#if far = smol face
faces = face_cascade.detectMultiScale(
    gray, #cray
    scaleFactor=1.1, #scanface reduce size
    minNeighbors=5, #beliwev area face 5 round
    minSize=(30, 30))#interest object atlest 30x30 px

print(f"Face foudn: {len(faces)}")
#draw frame numhenrhumen
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w , y+h), (0, 255, 0), 2)
    
#resultseminectafys leihg jhikgfhhseutygrebjru h gjmnhtygbjmuniedkredhs bf ujdxyxfbyt rdxjukghezsjgfk jkds
cv2.imshow('Face Detection in Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()