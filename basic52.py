#SAVE RESIZED IMAGE
import cv2

cam=cv2.VideoCapture(0)
while True:
    rel, Frame=cam.read()
    cv2.imshow("Video",Frame)
    key=cv2.waitKey(1)
    resize = cv2.resize(Frame, (600, 600))
    if key == 67:
        cv2.imwrite("image_4.jpg",resize)
    if key == 27:
        break