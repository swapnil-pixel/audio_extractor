import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile
import os

st.title("Audio Extractor from Video")
st.write("Upload a video file, and this app will extract the audio for you!")

# Upload video file
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mkv", "mov", "avi"])

if uploaded_file:
    # Create a temporary file for the uploaded video
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_video_path = tmp_file.name

    # Extract audio
    with st.spinner("Extracting audio..."):
        video = VideoFileClip(tmp_video_path)
        audio_output_path = tmp_video_path + ".mp3"
        video.audio.write_audiofile(audio_output_path)
        
        video.close()
    
    # Offer download of the audio file
    with open(audio_output_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        st.download_button(label="Download extracted audio", data=audio_bytes, file_name="extracted_audio.mp3", mime="audio/mp3")
    
    # Clean up temporary files
    os.remove(tmp_video_path)
    os.remove(audio_output_path)

st.write("Upload a video and extract its audio in a few clicks!")
