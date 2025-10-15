import streamlit as st 
import cv2 
import time 
from face_detection_utils import detect_faces_and_capture

# Function to display the video stream page
def show_video_stream():
    st.title("Real-Time Face Detection with Frame Capture")
    st.sidebar.title("Options")

    # Sidebar options
    start_video = st.sidebar.button("Start Video Stream")
    stop_video = st.sidebar.button("Stop Video Stream")

    # Display area for video
    video_placeholder = st.empty()

    # Initialize the video capture
    cap = cv2.VideoCapture(0) 
    prev_time = time.time()

    if start_video:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                st.warning("Failed to read from the camera. Please check your device.")
                break

            # Process the frame and capture faces
            frame, prev_time = detect_faces_and_capture(frame, prev_time)

            # Display the frame
            video_placeholder.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

            # Stop the video on user request
            if stop_video:
                break

        cap.release()
        st.success("Video Stream Stopped")
    else:
        st.info("Click 'Start Video Stream' to begin.")
    