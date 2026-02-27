import pandas as pd
from streamlit_option_menu import option_menu
import streamlit as st
import os
from datetime import datetime
import cv2
import speech_recognition as sr
import threading
import csv

with st.sidebar:
    selected = option_menu("Admin Panel",["Dashboard","About us",""
                                                                 "Dataset","Project","Login","settings"],
                           icons=["cast","people","table","activity","lock","gear"],
                           menu_icon=["cast"],default_index=0,orientation="vertical")
if selected == "Dashboard":
    st.header("📊 ExamGuardian Dashboard")
    st.write(
        "Welcome to the ExamGuardian Dashboard — your ultimate hub for next-level, AI-powered exam security! "
        "Leverage cutting-edge video and audio analysis to instantly spot suspicious activities like glancing away, multiple faces,"
        " or unauthorized conversations. "
        "Stay one step ahead with real-time alerts and automated incident logs that put you in full control of exam integrity. "
        "Experience effortless, reliable, and intelligent proctoring — making online exams safer, fairer, and smarter than ever before."
    )


if selected == "About us":
    st.header("🎯 About ExamGuardian")
    st.write("""
    ExamGuardian is an advanced AI-powered proctoring solution designed to maintain the integrity of online examinations.
     By combining real-time video and audio analysis,
     ExamGuardian ensures a secure and fair testing environment for candidates and educators alike.

    ### 🔑 Key Features:
    - **Dashboard & Dataset Viewer:** Access exam activity logs and review detailed records from `surveillance_alerts.csv`.
    - **Real-Time Video Surveillance:** Detects faces, monitors head movements (left/right), and flags multiple faces to catch potential cheating.
    - **Audio Monitoring:** Captures and analyzes spoken words during the exam to identify unauthorized conversations.
    - **Instant Alerts:** Provides immediate, on-screen warnings for suspicious behavior, and logs incidents with precise timestamps.
    - **Secure Admin Login:** Protects the system with a basic authentication feature for authorized personnel.
    - **Streamlit-Based Web Interface:** Offers an intuitive and interactive dashboard for easy management and monitoring.

    ### ✅ Advantages:
    - **Comprehensive Exam Security:** Combines multiple AI techniques to detect cheating behaviors effectively.
    - **Automated Evidence Collection:** Logs incidents automatically for reliable post-exam review and documentation.
    - **Cost-Effective Proctoring:** Reduces the need for manual invigilators, lowering operational costs.
    - **Scalable & Flexible:** Easily deployable for institutions of any size with a standard webcam and microphone.
    - **User-Friendly Experience:** Simplifies exam monitoring through a modern, web-based interface accessible from any device.
    """)





if selected == "Dataset":
        st.header("Dataset📁")
        df = pd.read_csv("surveillance_alerts.csv")
        st.dataframe(df)

if selected =="Project":

    st.header("ExamGuardian: Real-Time AI Surveillance for Online Exams 🚀")
    st.title("ExamGuardian AI Surveillance🛡️")
    if st.button("Start"):






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
            st.write("[INFO] Audio surveillance started.")
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
                        st.warning(f"[ALERT] {alert_message}")
                except sr.UnknownValueError:
                    pass
                except Exception as e:
                    st.write(f"[ERROR] Audio: {e}")


        threading.Thread(target=audio_detection, daemon=True).start()

        st.write("[INFO] Video surveillance started. Press 'q' to quit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                st.write("[ERROR] Cannot access webcam!")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) > 0:
                if len(faces) > 1:
                    alert_message = "ALERT: Multiple faces detected!"
                    log_alert("Multiple Faces Detected")
                    st.warning("[ALERT] Multiple faces detected!")

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    face_center = (x + w // 2, y + h // 2)

                    if face_center_prev is not None:
                        dx = face_center[0] - face_center_prev[0]

                        if abs(dx) > CENTER_TOLERANCE_X:
                            if dx > 0:
                                alert_message = "ALERT: Head moved right!"
                                log_alert("Head Movement", "Right")
                                st.warning("[ALERT] Head moved right!")
                            else:
                                alert_message = "ALERT: Head moved left!"
                                log_alert("Head Movement", "Left")
                                st.warning("[ALERT] Head moved left!")

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


if selected == "Login":
    st.header("🔐 Admin Login")
    st.write("Please enter your admin credentials below:")

    with st.form(key="login_form"):
        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")
        login_btn = st.form_submit_button("Login")

    if login_btn:
        if username == "abc123" and password == "1234":
            st.success("✅ Login successful! Welcome, Admin.")
        else:
            st.error("❌ Invalid username or password. Please try again.")

if selected == "settings":
    st.header("⚙️ Settings")
    st.info("Settings panel is under development. Future updates will include:")
    st.markdown("""
    - 🔄 **Change Admin Password**
    - 🎨 **Customize Dashboard Theme**
    - 📝 **Manage User Permissions**
    - 📡 **Configure Notification Settings**
    - 🗃️ **Data Storage Options**
    """)

