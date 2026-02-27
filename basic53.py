import cv2
import time

cam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("Video,avi",fourcc,20,(640,480))

start_time = time.time()
while(int(time.time() - start_time) < 15):
    r,Frame = cam.read()
    cv2.imshow("Video",Frame)
    out.write(Frame)
    cv2.waitKey(1)
cam.release()
out.release()
cv2.destroyAllWindows()
