import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_front_face_default.xml')

people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']

# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_recognizer.yml')


image = cv.imread('Faces/val/ben_afflek/5.jpg')
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)
 
#detect the face
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
for (x,y,w,h) in faces_rect:
    face_roi = gray[y:y+h,x:x+w]
    label, confidence = face_recognizer.predict(face_roi)
    print(f'Label = {people[label]} with confidence of {confidence}')
    cv.putText(image, str(people[label]), (30,30), cv.FONT_HERSHEY_COMPLEX,1.1,(0,255,0), thickness=2)
    cv.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)

cv.imshow('DetectedFace',image)

cv.waitKey(0)