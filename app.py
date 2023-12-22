import streamlit as st
# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
import soundfile as sf

st.title('Audio to Text')  # 타이틀명 지정
st.write("")

audio_m4a = st.file_uploader('녹음파일(wav)을 업로드 하세요.', type=['wav'])

# create a speech recognition object
r = sr.Recognizer()

#음원을 segment로 분할하는 기준 시간 (분). 음원을 통째로 분석하는것이 어려워 분할이 필요함.
len_seg = 300

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    # open the audio file using pydub
    folder_name = path.replace("wav","")
    fh = open(folder_name+"txt", "w+") 
    sound = AudioSegment.from_wav(path)
    duration = len(sound) / 1000
    whole_text = ""
    
    # create a directory to store the audio chunks   
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
      
    # split audio sound
    for i in range(int(duration//len_seg+1)):  
        globals()['start_time_'+str(i)] = len_seg*(i)
        globals()['end_time_'+str(i)]  = len_seg*(i+1)
        if globals()['end_time_'+str(i)] > duration:
            globals()['end_time_'+str(i)] = duration
     
        globals()['segment_'+str(i)] = sound[globals()['start_time_'+str(i)]*1000:globals()['end_time_'+str(i)]*1000]
          
        # process each chunk 
        # export audio chunk and save it in the `folder_name` directory.
        seg_filename = os.path.join(folder_name, f"seg{i}.wav")
        globals()['segment_'+str(i)].export(seg_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(seg_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened, language='ko-KR')
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                #text = f"{text.capitalize()}. "
                print(" -- :", text)
                #whole_text += str(i+1)+"/"+str(int(duration//len_seg+1))+"번째 본문입니다"+"\n"+text+"\n"+"\n"
                whole_text += text+"\n"
                
    # return the text for all chunks detected
    fh.write(whole_text+"\n") 
    return whole_text

print("\nFull text:", get_large_audio_transcription(path_wav))    
