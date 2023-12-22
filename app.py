import streamlit as st
# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
import soundfile as sf

#st.title('Audio to Text')  # 타이틀명 지정
#st.write("")

#audio_m4a = st.file_uploader('녹음파일(m4a)을 업로드 하세요.', type=['m4a'])

# create a speech recognition object
#r = sr.Recognizer()


import streamlit as st
import speech_recognition as sr
import os
import math

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

def main():
    st.title("Audio to Text Converter")

    # Upload the audio file
    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "ogg"])

    if audio_file is not None:
        # Split the audio file into 5-minute chunks
        CHUNK_DURATION = 5 * 60 # 5 minutes
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio_duration = math.ceil(source.DURATION)
            num_chunks = math.ceil(audio_duration / CHUNK_DURATION)
            for i in range(num_chunks):
                chunk_start = i * CHUNK_DURATION
                chunk_end = min((i + 1) * CHUNK_DURATION, audio_duration)
                audio_text = r.record(source, offset=chunk_start, duration=chunk_end-chunk_start)
                text = r.recognize_google(audio_text)

                # Display the text for this chunk
                st.header(f"Text from Audio (Chunk {i+1}/{num_chunks})")
                st.write(text)


if __name__ == '__main__':
    main()
