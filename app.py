import streamlit as st
# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
import soundfile as sf

st.title('Audio to Text')  # 타이틀명 지정
st.write("")

audio_m4a = st.file_uploader('녹음파일(m4a)을 업로드 하세요.', type=['m4a'])

# create a speech recognition object
r = sr.Recognizer()
