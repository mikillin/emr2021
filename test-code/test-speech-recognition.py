# https://www.youtube.com/watch?v=K_WbsFrPUCk
# pip install SpeechRecognition

# FOR WINDOWS USER
# pip install pipwin
# pipwin install pyaudio

# TESTED AND WORKED (Yosua Kurniawan) 8.8.2021

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")