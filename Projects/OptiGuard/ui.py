import streamlit as st
import os
from form import show_form

# Create "DB" and "Storage" folders if they don't exist
if not os.path.exists("DB"):
    os.makedirs("DB")
if not os.path.exists("Storage"):
    os.mkdir("Storage")


# Main function to manage navigation
def main():
    if "page" not in st.session_state:
        st.session_state.page = "form"
    if st.session_state.page == "form":
        show_form()
    elif st.session_state.page == "video_stream":
        from video import show_video_stream
        import shutil
        show_video_stream()
        if st.button("Delete All Data, Back to Form"):
            shutil.rmtree("DB") 
            shutil.rmtree("Storage")
            st.session_state.page = "form"


if __name__ == "__main__":
    main()

''' 
python3.11 -m streamlit run ui.py
'''