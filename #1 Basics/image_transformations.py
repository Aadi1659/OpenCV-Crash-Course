import cv2 as cv
import numpy as np

image = cv.imread("2.jpg")
cv.imshow("Cat",image)

def translate(image,x,y):
    #we have to make a translation matrix first to specifty the translation values
    transMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (image.shape[1],image.shape[0]) #height,width
    return cv.warpAffine(image,transMatrix,dimensions)

'''
x --> right
y --> down
-x --> left
-y --> up
'''

translated = translate(image,-100,100)
cv.imshow("Translated Image",translated)

#Rotation
def rotate(image, angle, rotatePoint = None):
    (height,width) = image.shape[:2]
    if rotatePoint is None:
        rotatePoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotatePoint,angle,1.0) #1.0 is the scaling factor
    dimensions = (width, height)
    
    return cv.warpAffine(image,rotMat,dimensions)

rotated = rotate(image,90)
cv.imshow("Rotated Image",rotated)

#Flipping
flip0 = cv.flip(image,0) #verical flip
flip1= cv.flip(image,1) #horizontal flip
flipneg1 = cv.flip(image,-1) #both

cv.imshow("Vertical Flip",flip0)
cv.imshow("Horizontal Flip",flip1)
cv.imshow("Both Flip",flipneg1)

cv.waitKey(0)
