import cv2

cam = cv2.VideoCapture(0)
while True:
        rel,Frame = cam.read()
        cv2.imshow("Video",Frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
