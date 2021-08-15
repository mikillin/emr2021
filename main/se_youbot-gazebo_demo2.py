########################################
# EMR 2021 PROJEKT - SPRACH EREKENNUNG #
########################################

# Mitglieder:

#     Marcel Heinen
#     Sergey Rogachevsky
#     Yosua Kurniawan

# se_youbot-gazebo_demo1.py Python 3.8.10 tested and works (15.08.2021) 

# Known Issues:

# none so far

# Library:

# Speech Recognition:

#     $ pip install SpeechRecognition

# FOR WINDOWS USER NEED TO ADD:

#     $ pip install pipwin
#     $ pipwin install pyaudio

# Package:

# rospy:

#     $ sudo apt install python-rospy

# pyaudio:

#     $ sudo apt install python3-pyaudio


# Terminal:

# $ roscore
# $ ~/catkin_ws/src/emr/emr_youbot/launch
# $ roslaunch youbot_emr_simulation_empty_gazebo.launch

######################################################################

import speech_recognition as sr
from geometry_msgs.msg import Twist
import rospy
import time

x=0
y=0
yaw=0


def init():
    global msg, velocity_publisher, pose_subscriber

    msg = Twist()
    msg.linear.x = 0
    msg.linear.y = 0
    msg.angular.x = 0
    msg.angular.y = 0

    try:
        
        rospy.init_node('se_youbot', anonymous=True)

        #declare velocity publisher
        cmd_vel_topic = "/cmd_vel"
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        time.sleep(2)
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")

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


def phrasing_audio_direction():
    text_lst_direction = ""
    direction = ""
    determine_direction = True

    while determine_direction: 
        print("Give direction input (forward, backward, left, right) :")
        text_lst_direction = get_audio()
        if "forward" in text_lst_direction:
            print("Moving Forward")
            direction = "forward"
            determine_direction = False
            return direction
        elif "backward" in text_lst_direction:
            print("Moving Backward")
            direction = "backward"
            determine_direction = False
            return direction
        elif "left" in text_lst_direction:
            print("Turning Left")
            direction = "left"
            determine_direction = False
            return direction
        elif "right" in text_lst_direction:
            print("Turning Right")
            direction = "right"
            determine_direction = False
            return direction
        elif "stop" in text_lst_direction:
            print("Stop")
            direction = "stop"
            determine_direction = False
            return direction  
        elif "exit" in text_lst_direction:
            print("Exit Program")
            direction = "exit"
            determine_direction = False
            return direction           
        else:
            print("UNABLE TO RECOGNIZE COMMAND TRY AGAIN")
            determine_direction = True

def move():
        #declare a Twist message to send velocity commands
        msg = Twist()

        global x, y, speed

        speed = 0.1 # define the speed of turtle
        direction = "INITIAZION SUCSESS, AWAITING ORDER" # INITIAZION

        loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
        cmd_vel_topic = '/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        while True :
                rospy.loginfo("youBot move: " + direction)
                velocity_publisher.publish(msg)

                loop_rate.sleep()
                direction = phrasing_audio_direction()
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
                elif  direction == "exit":
                    rospy.loginfo("Exit Program")
                    break
        
        #finally, stop the robot when quit the program
        msg.linear.x =0
        msg.linear.y =0
        velocity_publisher.publish(msg)

if __name__ == '__main__':

    init()
    move()

