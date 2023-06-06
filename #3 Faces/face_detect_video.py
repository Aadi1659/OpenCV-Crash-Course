import cv2 as cv

haar_cascade = cv.CascadeClassifier("haar_front_face_default.xml")

video_capture = cv.VideoCapture("group.mp4")

# Get the video's frame width, height, and frames per second
frame_width = int(video_capture.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = video_capture.get(cv.CAP_PROP_FPS)

# Create a VideoWriter object to save the output video
output_video = cv.VideoWriter("output_video.mp4",
                              cv.VideoWriter_fourcc(*"mp4v"),
                              fps,
                              (frame_width, frame_height))

while True:
    # Read the current frame
    ret, frame = video_capture.read()

    # Break the loop if the video has ended
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv.imshow("Faces", frame)

    output_video.write(frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and video writer objects
video_capture.release()
output_video.release()

cv.waitKey(0)