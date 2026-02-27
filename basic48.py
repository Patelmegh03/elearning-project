import cv2

cam = cv2.VideoCapture(0)
while True:
        rel,Frame = cam.read()
        gray =  cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Video",gray)
        key = cv2.waitKey(1)
        if key == 27:
            break