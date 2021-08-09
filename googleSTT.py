import speech_recognition as sr
import _thread
from geometry_msgs.msg import Twist
import rospy

global msg


def init():
    global msg

    msg = Twist()
    msg.linear.x = 0
    msg.linear.y = 0
    msg.linear.x = 0
    msg.angular.z = 0


def recognition():
    global msg

    sample_rate = 48000
    chunk_size = 2048
    r = sr.Recognizer()
    with sr.Microphone(device_index=1, sample_rate=sample_rate,
                       chunk_size=chunk_size) as source:
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        # while not rospy.is_shutdown():
        while text != "end":
            audio = r.listen(source)

            try:
                # language =
                #text = r.recognize_google(audio, "None", language : "de-DE")
                # r.recognize_google(audio, language="de-DE")
                r.recognize_google(audio)
                # text = r.recognize_google(audio)
                #text = r.recognize_sphinx(audio)
                print("you said: " + text)
                if text == "links":
                    msg.angular.z = 1
                elif text == "links":
                    msg.angular.z = -1

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0} ".format(e))
    return text


def publisher():
    global msg
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('robotControl', anonymous=True)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    global msg
    init()

    text = ""
    try:
        _thread.start_new_thread(publisher, ())
        _thread.start_new_thread(recognition, ())
        # _thread.start_new_thread(recognition, ())
    except:
        print ("Error: unable to start thread")

    #while text != "end":
    #    text = recognition()
