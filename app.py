import streamlit as st
# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
import soundfile as sf

st.title('Audio to Text')  # 타이틀명 지정
st.write("")

audio_m4a = st.file_uploader('녹음파일(m4a)을 업로드 하세요.', type=['m4a'])


#filename = input("Text로 변환하려고하는 녹음파일(m4a)의 이름을 입력하세요  \n")    


#filename = input("Text로 변환하려고하는 녹음파일(m4a)의 이름을 입력하세요  \n")    

# m4a 파일 경로
path_m4a = audio_m4a

# wav 파일 경로
path_wav = converted+".wav"

# m4a 파일 로드
#audio_m4a = AudioSegment.from_file(path_m4a, format="m4a")

# wav 파일로 변환
audio_wav = audio_m4a.export(path_wav, format="wav")

