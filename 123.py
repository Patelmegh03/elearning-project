import cv2, numpy as np, speech_recognition as sr, threading, time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
CENTER_TOLERANCE_X, face_center_prev, alert_message, lock = 80, None, "", threading.Lock()

def audio_detection():
    global alert_message
    r, mic = sr.Recognizer(), sr.Microphone()
    with mic as src: r.adjust_for_ambient_noise(src)
    while True:
        try:
            with mic as src: text = r.recognize_google(r.listen(src, phrase_time_limit=3)).strip()
            if text:
                with lock: alert_message = f"Voice detected: {text}"
                print("[ALERT]", alert_message)
        except sr.UnknownValueError: pass
        except Exception as e: print("[ERROR]", e)

threading.Thread(target=audio_detection, daemon=True).start()
print("[INFO] Surveillance started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret: break
    gray, alert_message = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), ""
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        if len(faces) > 1:
            with lock: alert_message = "ALERT: Multiple faces detected!"
            print("[ALERT] Multiple faces detected!")
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)
            fc = (x + w//2, y + h//2)
            if face_center_prev:
                dx = fc[0] - face_center_prev[0]
                if abs(dx) > CENTER_TOLERANCE_X:
                    with lock:
                        alert_message = "ALERT: Head moved right!" if dx > 0 else "ALERT: Head moved left!"
                    print("[ALERT]", alert_message)
            face_center_prev = fc
    else:
        face_center_prev = None

    with lock:
        if alert_message:
            cv2.putText(frame, alert_message, (20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

    cv2.imshow('ExamGuardian AI', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
