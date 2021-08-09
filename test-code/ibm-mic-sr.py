from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import speech_recognition as sr
apikey = ''
url = ''

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

print("Authentication Sucsess")

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    res = stt.recognize(audio=source, content_type='audio/wav', model='en-US_NarrowbandModel', continuous=True).get_result()
    
text = res['results'][0]['alternatives'][0]['transcript']
print(text)

    # audioin = r.listen(source)
    # try:
    #     res = stt.recognize(audio=audioin, content_type='audio/wav', model='en-US_NarrowbandModel', continuous=True).get_result()
    #     text = res['results'][0]['alternatives'][0]['transcript']
    #     print(text)
    # except:
    #     print("Sorry could not recognize what you said")
