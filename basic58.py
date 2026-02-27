import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread("C:/Users/Admin/PyCharmMiscProject/image_04.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_Detect = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
print(face_Detect)
for (x, y, w, h) in face_Detect:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Face Detect", img)
cv2.waitKey(0)
cv2.destroyAllWindows()