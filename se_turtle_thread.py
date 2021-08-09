import speech_recognition as sr
import _thread
from geometry_msgs.msg import Twist
import rospy

global msg, pub


def init():
    global msg, pub

    msg = Twist()
    msg.linear.x = 0
    msg.linear.y = 0
    msg.angular.z = 0

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('se_turtle', anonymous=True)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = ""
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print("Unrecognizeable")
    return text


def speechRecognition():
    global msg, pub
    text_lst = ""
    while text_lst != "end":
        print("Befehlen Sie bitte:")
        text_lst = get_audio()

        if "1" in text_lst:
            print("Moving Forward")
            msg.linear.x = 0.1
            msg.linear.y = 0
            msg.angular.z = 0
        elif "2" in text_lst:
            print("Moving Backward")
            msg.linear.x = -0.1
            msg.linear.y = 0
            msg.angular.z = 0
        elif "3" in text_lst:
            print("Turning Left")
            msg.linear.x = 0
            msg.linear.y = 0.1
            msg.angular.z = 0
        elif "4" in text_lst:
            print("Turning Right")
            msg.linear.x = 0
            msg.linear.y = -0.1
            msg.angular.z = 0
        elif "5" in text_lst:
            print("Stop Movement")
            msg.linear.x = 0
            msg.linear.y = 0
            msg.angular.z = 0
        else:
            print("UNABLE TO RECOGNIZE COMMAND")
            msg.linear.x = 0
            msg.linear.y = 0
            msg.angular.z = 0

def publishOrder():
    global msg, pub

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    global msg
    init()

    try:
        _thread.start_new_thread(publishOrder, ())
        _thread.start_new_thread(speechRecognition, ())
    except:
        print("Error: unable to start thread")
