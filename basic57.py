import numpy as np
import cv2

canvas = np.ones((500,500,3),dtype="uint8")*255
cv2.line(canvas, (50,50), (350, 50), (255,75, 98),2)
cv2.rectangle(canvas, (100, 100), (250,450), (215,255,14),2)


cv2.imshow("CANVAS",canvas)
cv2.waitKey()