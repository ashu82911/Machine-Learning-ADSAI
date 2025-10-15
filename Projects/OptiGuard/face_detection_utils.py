import cv2
import time
import mediapipe as mp
import pandas as pd 
from collections import defaultdict
import face_recognition
import streamlit as st

data = pd.read_csv("DB/appointments.csv")
out_time = pd.to_datetime(list(data["Out Date and Time"])[-1]).strftime("%d%m%Y_%H%M%S")
flag = False
person_dict = defaultdict()

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def detect_faces_and_capture(frame, prev_time, capture_interval = 5, storage_folder="Storage"):
    """
    Detect faces in the frame, draw bounding boxes, and capture frames periodically.

    Parameters:
        frame (ndarray): The video frame to process.
        prev_time (float): The timestamp of the last captured frame.
        capture_interval (int): Interval in seconds for capturing frames.
        storage_folder (str): Folder to save captured frames.

    Returns:
        tuple: Processed frame and updated timestamp.
    """
    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Initialize face detection model
    with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(rgb_frame)

        # Draw bounding boxes if faces are detected
        if results.detections: # 3 faces
            st.session_state["error"] = False
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box 
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                
                # Extract the face region
                face_region = frame
                
                # Convert the face region to RGB
                rgb_face_region = cv2.cvtColor(face_region, cv2.COLOR_BGR2RGB)
                
                # Encode the face region
                face_encodings = face_recognition.face_encodings(rgb_face_region)

                known_face_image = face_recognition.load_image_file(file = f"DB/{data.iloc[0]['Name']}_{data.iloc[0]['Phone No.']}.jpg")
                known_face_encodings = face_recognition.face_encodings(known_face_image)
                
                if face_encodings and known_face_encodings:
                    # Compare with the submitted face encoding
                    matches = face_recognition.compare_faces(known_face_encodings, face_encodings[0], tolerance=0.4)
                    if matches[0]:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # green rectangle
                    else:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) # red rectangle
                else:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) # red rectangle if no encoding found

            # Capture a photo every capture_interval seconds
            current_time = time.time()
            global flag
            if int(current_time - prev_time) > capture_interval:
                timestamp = time.strftime("%d%m%Y_%H%M%S")
                if pd.to_datetime(timestamp, format="%d%m%Y_%H%M%S") >= pd.to_datetime(out_time, format="%d%m%Y_%H%M%S"):
                    flag = True
                if flag:
                    cv2.putText(frame, "Get Out Now", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2, cv2.LINE_AA)
                else:
                # Get current timestamp for the photo filename
                    photo_filename = f"{storage_folder}/{timestamp}.jpg"
                    cv2.imwrite(photo_filename, frame)
                    person_dict[str(f"{data['Name'].iloc[-1]}_{data['Phone No.'].iloc[-1]}_{data['Appointment Date and Time'].iloc[-1]}")] = timestamp
                    prev_time = current_time
        else:
            cv2.putText(frame, "Face not visible", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    pd.DataFrame({"keys": list(person_dict.keys()), "Timestamp": list(person_dict.values())}).to_csv("DB/person_map.csv")
    return frame, prev_time
