import cv2

# Initialize camera image
video = cv2.VideoCapture(0)
check, frame = video.read()

# Video loop
while check:
    # Launching video
    check, frame = video.read()
    cv2.imshow("Gesture recognition 2.0", frame)

    # Defining stopping requirement
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Destroying
video.release()
cv2.destroyAllWindows()