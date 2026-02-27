import cv2
import speech_recognition as sr
import threading
import csv
import os
from datetime import datetime

csv_filename = "surveillance_alerts.csv"
if not os.path.exists(csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Alert Type", "Details"])

def log_alert(alert_type, details=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, alert_type, details])

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

CENTER_TOLERANCE_X = 80
face_center_prev = None
alert_message = ""

def audio_detection():
    global alert_message
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("[INFO] Audio surveillance started.")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
    while True:
        with mic as source:
            audio = recognizer.listen(source, phrase_time_limit=3)
        try:
            text = recognizer.recognize_google(audio)
            if text.strip():
                alert_message = f"Voice detected: {text}"
                log_alert("Voice Detected", text)
                print(f"[ALERT] {alert_message}")
        except sr.UnknownValueError:
            pass
        except Exception as e:
            print(f"[ERROR] Audio: {e}")

threading.Thread(target=audio_detection, daemon=True).start()

print("[INFO] Video surveillance started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Cannot access webcam!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        if len(faces) > 1:
            alert_message = "ALERT: Multiple faces detected!"
            log_alert("Multiple Faces Detected")
            print("[ALERT] Multiple faces detected!")

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            face_center = (x + w // 2, y + h // 2)

            if face_center_prev is not None:
                dx = face_center[0] - face_center_prev[0]

                if abs(dx) > CENTER_TOLERANCE_X:
                    if dx > 0:
                        alert_message = "ALERT: Head moved right!"
                        log_alert("Head Movement", "Right")
                        print("[ALERT] Head moved right!")
                    else:
                        alert_message = "ALERT: Head moved left!"
                        log_alert("Head Movement", "Left")
                        print("[ALERT] Head moved left!")

            face_center_prev = face_center

    if alert_message:
        cv2.putText(
            frame, alert_message, (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2
        )

    cv2.imshow('ExamGuardian AI Surveillance', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
