import cv2 as cv

def resizeImage(image,scale=0.75):
    height = image.shape[1]
    width = image.shape[0]

    dimension = (int(height*scale),int(width*scale))

    return cv.resize(image,dimension,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #Live video only (webcamera video running live)
    capture.set(3,width)
    capture.set(4,height)

#IMAGE
img = cv.imread("1.jpg")

resized_image = resizeImage(img,scale=0.2)

#uncomment the following lines for the images
# cv.imshow("Parking" , img)
# cv.imshow("Resized Parking", resized_image)
# cv.waitKey(0)

#VIDEO
capture = cv.VideoCapture("1.mp4")

while True:

    isTrue, frame = capture.read()
    resized_frame = resizeImage(frame,scale=0.2)
    if isTrue:
        cv.imshow("frame", frame)
        cv.imshow("resized_frame", resized_frame)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break

capture.release()
capture.destroyAllWindows()

