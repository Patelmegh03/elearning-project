import cv2
import os

output_dir = "Captured_Images"
os.makedirs(output_dir, exist_ok=True)

cam = cv2.VideoCapture(0)

ret, frame = cam.read()

original_path = os.path.join(output_dir, "original.jpg")
cv2.imwrite(original_path, frame)

blur = cv2.blur(frame, (15,15))
blur_path = os.path.join(output_dir, "blur.jpg")
cv2.imwrite(blur_path, blur)

gaussian_blur = cv2.GaussianBlur(frame,(15,15),0)
gaussian_path = os.path.join(output_dir, "gaussian_blur.jpg")
cv2.imwrite(gaussian_path, gaussian_blur)

median = cv2.medianBlur(frame, 5)
cv2.imwrite(os.path.join(output_dir, "median_blur.jpg"), median)

cv2.imshow("Original", frame)
cv2.imshow("Blur", blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median", median)

cv2.waitKey(0)
cv2.destroyAllWindows()