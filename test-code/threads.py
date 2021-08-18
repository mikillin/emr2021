import speech_recognition as sr
import _thread
from geometry_msgs.msg import Twist
import rospy

#global msg, pub

def init():
    global msg, pub

    msg = Twist()
    msg.linear.x = 0
    msg.linear.y = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0

    pub = rospy.Publisher('/turtle/cmd_vel', Twist, queue_size=10)
    rospy.init_node('se_turtle', anonymous=True)


def get_audio():
    r = sr.Recognizer()
    print(r.adjust_for_ambient_noise)
    print("1")

    with sr.Microphone() as source:
        audio = r.listen(source)
        text = ""
   
        print("1")
        try:
            text = r.recognize_sphinx(audio)
            print("2")
            print(text)
        except:
          print("Unrecognizeable")
    print("3")
    return text


def speechRecognition():
    global msg, pub
    text_lst = ""
    speed = 0.1

    while text_lst != "exit":
        print("Befehlen Sie bitte:")
        direction = get_audio()
        if direction == 'forward':
            msg.linear.x = abs(speed)
            msg.linear.y = 0
        elif direction == 'backward':
            msg.linear.x = -abs(speed)
            msg.linear.y = 0
        elif direction == 'left':
            msg.linear.x = 0
            msg.linear.y = abs(speed)
        elif direction == 'right':
            msg.linear.x = 0
            msg.linear.y = -abs(speed)
        elif direction == 'stop':
            msg.linear.x = 0
            msg.linear.y = 0     
            msg.angular.x = 0
            msg.angular.y = 0
            msg.angular.z = 0     
        elif direction == 'clockwise':
            msg.linear.x = 0
            msg.linear.y = 0
            msg.angular.x = -abs(speed)       
            msg.angular.y = -abs(speed)       
            msg.angular.z = -abs(speed)       
        elif direction == 'counter':
            msg.linear.x = 0
            msg.linear.y = 0 
            msg.angular.x = abs(speed)
            msg.angular.y = abs(speed)
            msg.angular.z = abs(speed)
        elif  direction == "exit":
            msg.linear.x = 0
            msg.linear.y = 0
            msg.angular.x = 0
            msg.angular.y = 0
            msg.angular.z = 0
            
    rospy.loginfo("Exit Program")
    # break
    
    # finally, stop the robot after exit
    msg.linear.x = 0
    msg.linear.y = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0
    
def publishOrder():
    global msg, pub

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    
    global msg, pub
    print("Hello world!`")
    init()

    try:
        _thread.start_new_thread(publishOrder, ())
        _thread.start_new_thread(speechRecognition, ())
    except:
        print("Error: unable to start thread")
