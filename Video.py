import cv2


class Video:
    def __init__(self):
        # Initialize camera image
        self.video = cv2.VideoCapture(0)

    def video_launch(self):
        while True:
            # Launching video
            check, frame = self.video.read()
            cv2.imshow("Gesture recognition 2.0", frame)

            # Defining stopping requirement
            key = cv2.waitKey(1)
            if key == ord('q'):
                self.video_destroy()
                break

    def video_destroy(self):
        self.video.release()
        cv2.destroyAllWindows()
