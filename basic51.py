import cv2

cam=cv2.VideoCapture(0)
while True:
    rel, Frame=cam.read()
    resize=cv2.resize(Frame, (400,400))
    cv2.imshow("Video",resize)
    key=cv2.waitKey(1)
    if key == ord('c'):
        cv2.imwrite("Image_3.jpg", Frame)

    if key == 27:
        break