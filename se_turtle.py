import speech_recognition as sr
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
        # print("Speak Anything :")
        audio = r.listen(source)
        text = ""
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print("Unrecognizeable")
    return text


def start_get_audio():
    global msg, pub
    text_lst = ""
    while text_lst != "end":
        print("Speak Anything :")
        text_lst = get_audio()

        if "1" in text_lst:
            print("Moving Forward")
            msg.linear.x = 0.1
        elif "2" in text_lst:
            print("Moving Backward")
            msg.linear.x = -0.1
        elif "3" in text_lst:
            print("Turning Left")
            msg.linear.y = 0.1
        elif "4" in text_lst:
            print("Turning Right")
            msg.linear.y = -0.1
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

        pub.publish(msg)

if __name__ == '__main__':
    global msg
    init()
    start_get_audio ()
