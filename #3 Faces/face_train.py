import cv2 as cv
import numpy as np
import os

people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']

p = []
DIR = 'Faces/train'

haar_cascade = cv.CascadeClassifier('haar_front_face_default.xml')

# for i in os.listdir(DIR):
#     p.append(i)
# print(p)

features = []
labels = []

#converting the image to numerical format to reduce the strain on our computer
def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)    
        # print(f"Path: {path},label:{label}")

        for image in os.listdir(path):
            image_path = os.path.join(path,image)
            image_array = cv.imread(image_path)
            gray = cv.cvtColor(image_array,cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print(f"Length of the features is {len(features)} and length of the labels is {len(labels)}")

face_recognizer = cv.face.LBPHFaceRecognizer_create()

features = np.array(features,dtype='object')
labels = np.array(labels)

#train the recognizer on the features list and lables list
face_recognizer.train(features,labels)
    
face_recognizer.save('face_recognizer.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)
print("Saving done.............")
