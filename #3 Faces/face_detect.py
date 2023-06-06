import cv2 as cv

image = cv.imread("4.jpg")
cv.imshow("Man",image)

#Face detection doesnt take into account the skin tone of  the human, its bette to make the image grayscale

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

haar_cascade = cv.CascadeClassifier("haar_front_face_default.xml")

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1555,minNeighbors=9)
print(f"Number of faces found = {len(faces_rect)}")

for (x,y,w,h) in faces_rect:
    cv.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow("Faces",image)

cv.waitKey(0)