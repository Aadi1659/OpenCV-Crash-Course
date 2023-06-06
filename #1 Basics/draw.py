import cv2 as cv
import numpy as np

#Drawing

#making a blank canvas
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow("Blank",blank)

#Paint
blank[200:300,300:400] = 0,255,0
cv.imshow("Green",blank)

#Square 
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=1)
cv.imshow("Square",blank)

#Rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]),(0,0,255),thickness=cv.FILLED)
cv.imshow("RED Rectangle",blank)
#note: blank.shape[1] returns height and blank.shape[0] returns width

#Circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(255,0,255),thickness=-1)
cv.imshow("Circle",blank)

#Line
cv.line(blank,(100,200),(150,280),(255,255,255),thickness=3)
cv.imshow("Line",blank)

#Text Custom
cv.putText(blank,"Hey there this is Aaditya!",(0,255),cv.FONT_HERSHEY_COMPLEX,1.0,(255,255,255),1)
cv.imshow("Text",blank)

cv.waitKey(0)