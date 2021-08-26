#!/usr/bin/env python
import speech_recognition as sr
import rospy
from std_msgs.msg import String


if __name__ == '__main__':
    # init()
    pub = rospy.Publisher('/se_befehl', String, queue_size=10)
    rospy.init_node('se_bot', anonymous=True)
    text =""
    while not rospy.is_shutdown():
        rObject = sr.Recognizer()
        audio = ''
        with sr.Microphone() as source:
            print("Sagen Sie..")
            audio = rObject.listen(source, phrase_time_limit=0)
            try:
                text = rObject.recognize_sphinx(audio) #rObject.recognize_google(audio) recognize_sphinx
                print("Sie haben gesagt : " + text)
                pub.publish(text)
            except:
                print("Es war zu unklar. Sagen Sie es wieder!")
