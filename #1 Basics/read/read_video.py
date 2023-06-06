import cv2 as cv

# capture = cv.VideoCapture(0) #make it 0 for accessing your webcamera

capture = cv.VideoCapture("1.mp4") #we need to display the video frame by frame now

while True:

    isTrue, frame = capture.read() #this returns a boolean stating whether the capture was successful or not and returns the frame number

    if isTrue:
        cv.imshow("frame", frame)
        if cv.waitKey(20) & 0xFF == ord('q'): #if the user pressed q
            break

capture.release()
capture.destroyAllWindows()