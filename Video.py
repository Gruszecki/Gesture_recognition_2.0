import cv2


class Video:
    def __init__(self):
        # Initialize camera image
        self.video = cv2.VideoCapture(0)

    def video_launch(self):
        while True:
            # Launching video
            check, frame = self.video.read()                # Read image
            frame = image_conversion(frame)                 # Image conversion
            cv2.imshow("Gesture recognition 2.0", frame)    # Show image

            # Defining stopping requirement
            key = cv2.waitKey(1)
            if key == ord('q'):
                self.__video_destroy()
                break

    def __video_destroy(self):
        self.video.release()
        cv2.destroyAllWindows()


def image_conversion(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                  # Convert to grayscale
    # frame = cv2.blur(frame, (8, 8))                                  # Blur
    # frame = cv2.threshold(frame, 80, 255, cv2.THRESH_BINARY_INV)[1]  # B&W
    # frame = cv2.Canny(frame, 100, 100)                               # Contours
    return frame
