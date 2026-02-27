import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

while True:
    rel, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)


    if len(faces) == 0:
        status = "No face detected (Suspicious)"
    elif len(faces) == 1:
        status = "One face detected (Normal)"
    else:
        status = f"{len(faces)} faces detected (Suspicious)"


    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


    cv2.putText(frame, status, (10, 30), cv2.COLOR_BGR2GRAY, 0.8, (0, 0, 255), 2)


    cv2.imshow("ExamGuardian - Surveillance", frame)


    if cv2.waitKey(1) == 27:
        break


cam.release()
cv2.destroyAllWindows()