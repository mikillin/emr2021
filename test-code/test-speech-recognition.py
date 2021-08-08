# https://www.youtube.com/watch?v=K_WbsFrPUCk
# pip install SpeechRecognition

# FOR WINDOWS USER
# pip install pipwin
# pipwin install pyaudio

# TESTED AND WORKED (Yosua Kurniawan) 8.8.2021

import speech_recognition as sr

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        text = ""
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print("Unrecognizeable")
    return text

text_lst = get_audio()

if "forward" in text_lst:
    print("Moving Forward")
elif "backward" in text_lst:
    print("Moving Backward")
elif "left" in text_lst:
    print("Turning Left")
elif "right" in text_lst:
    print("Turning Right")    
elif "stop" in text_lst:
    print("Stop Movement") 
else:
    print("UNABLE TO RECOGNIZE COMMAND") 