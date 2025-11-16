import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="Voice → Text", page_icon="🎤")

st.title("🎤 Simple Voice-to-Text Generator")
st.write("Upload an audio file and convert it to text using Whisper.")

# Load API key
api_key = st.text_input("Enter your OpenAI API Key", type="password")

uploaded_file = st.file_uploader(
    "Upload audio (mp3, wav, m4a)", 
    type=["mp3", "wav", "m4a"]
)

if uploaded_file and api_key:
    client = OpenAI(api_key=api_key)

    st.audio(uploaded_file)

    if st.button("Transcribe"):
        with st.spinner("Transcribing..."):
            audio_bytes = uploaded_file.read()
            with open("temp_audio", "wb") as f:
                f.write(audio_bytes)

            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=open("temp_audio", "rb")
            )

        st.success("Transcription Complete!")
        st.text_area("Transcribed Text", transcription.text, height=200)
