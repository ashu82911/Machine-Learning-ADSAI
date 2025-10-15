import streamlit as st 
from datetime import datetime
import re
import os 
import pandas as pd

def show_form():
    st.title("Appointment Form")

    # Name input
    name = st.text_input("Name")

    # Phone number input with regex validation
    phone_no_pattern = re.compile(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")  # Example pattern for international phone numbers

    def validate_phone_no():
        if not phone_no_pattern.match(st.session_state.phone_no):
            st.session_state.phone_no_error = "Invalid phone number format. Please enter a valid phone number."
        else:
            st.session_state.phone_no_error = ""

    phone_no = st.text_input("Phone No.", key="phone_no", on_change=validate_phone_no)

    # Display phone number error if any
    if "phone_no_error" in st.session_state and st.session_state.phone_no_error:
        st.error(st.session_state.phone_no_error)

    # Image upload
    # image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    image = st.camera_input(label="Say cheese and click your photo")

    # Purpose text field
    purpose = st.text_area("Purpose")

    # Area to be visited drop down menu
    area = st.selectbox("Area to be visited", ["Area 1", "Area 2", "Area 3", "Area 4"])

    # Appointment date input
    appointment_date = st.date_input("Appointment Date")
    appointment_time = st.time_input("Appointment Time")
    out_time = st.time_input("Out Time", value=datetime.strptime("18:00", "%H:%M").time())

    # Combine date and time into a single datetime object
    appointment_datetime = datetime.combine(appointment_date, appointment_time)
    out_datetime = datetime.combine(appointment_date, out_time)


    # Submit button
    if st.button("Submit"):
        if name==None or phone_no==None or image==None or purpose==None or area==None\
        or appointment_date==None or appointment_time==None:
            st.error("Oops! you miss out something")
        elif not phone_no_pattern.match(phone_no):
            st.error("Invalid phone number format. Please enter a valid phone number.")
        else:
            # Save image to folder and get the path
            image_path = None
            if image is not None:
                image_path = os.path.join("DB", f'{name}_{phone_no}.jpg')
                with open(image_path, "wb") as f:
                    f.write(image.getbuffer())

            # Create a DataFrame and save to CSV
            data = {
                "Name": [name],
                "Phone No.": [phone_no],
                "Purpose": [purpose],
                "Area to be visited": [area],
                "Appointment Date and Time": [appointment_datetime],
                "Out Date and Time": [out_datetime],
                "Image Path": [image_path]
            }
            df = pd.DataFrame(data)

            # Append to CSV if it exists, otherwise create a new one
            csv_path = os.path.join("DB", "appointments.csv")
            if os.path.exists(csv_path):
                df.to_csv(csv_path, mode='a', header=False, index=False)
            else:
                df.to_csv(csv_path, index=False)

            st.success("Appointment details saved successfully!")
            st.session_state.page = "video_stream"
            st.rerun()