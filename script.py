from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
apikey = 'nym1d2uB6F8t1DFE-xbwyFUQb6_JgFlg-dgddUcUICo9'
url = 'https://api.eu-de.speech-to-text.watson.cloud.ibm.com/instances/bc6a421d-859e-41ff-b947-65728da01e49'

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

# Perform conversion
with open('c:/speech commands/happy/012c8314_nohash_0.wav', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/wav', model='en-US_NarrowbandModel', continuous=True).get_result()
    
text = res['results'][0]['alternatives'][0]['transcript']
print(text)
