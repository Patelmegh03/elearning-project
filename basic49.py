import cv2

cam = cv2.VideoCapture(0)
r, Frame = cam.read()
cv2.imwrite("Image_1.jpg",Frame)