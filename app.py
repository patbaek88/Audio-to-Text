import streamlit as st
# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
import soundfile as sf

st.title('Audio to Text')  # 타이틀명 지정
st.write("")

filename = st.file_uploader('녹음파일(m4a)을 업로드 하세요.', type=['m4a'])


#filename = input("Text로 변환하려고하는 녹음파일(m4a)의 이름을 입력하세요  \n")    
