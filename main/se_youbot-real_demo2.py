########################################
# EMR 2021 PROJEKT - SPRACH EREKENNUNG #
########################################

# Mitglieder:

#     Marcel Heinen
#     Sergey Rogachevsky
#     Yosua Kurniawan

# se_youbot-real_demo2.py Python 3.8.10 tested and works (26.08.2021) 

# Known Issues:
# time delay between Computer due to wireless connection (Real Robot when using wireless connectivity)
# awful sphinx audio accuracy

# Library and Packages:

# Speech Recognition:

#     $ pip install SpeechRecognition

# FOR WINDOWS USER NEED TO ADD:

#     $ pip install pipwin
#     $ pipwin install pyaudio

# FOR UBUNTU USER NEED TO ADD:

#     $ sudo apt-get install portaudio19-dev python3-pyaudio
#     $ pip install PyAudio

# pocketsphinx:

#     $ sudo apt install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev

#     $ sudo apt-get install swig3.0 or $ sudo apt-get install swig (only god knows)

#     $ sudo pip install pocketsphinx


# rospy:

#     $ sudo apt install python-rospy

# pyaudio:

#     $ sudo apt install python3-pyaudio

# In real youBot (the same as roscore terminal):

# roslaunch youbot_driver_ros_interface youbot_driver.launch

######################################################################
# import all required libraries
import speech_recognition as sr
from geometry_msgs.msg import Twist
import rospy
import time
# define initial position of the robot
x=0
y=0
z=0
yaw=0

# initiate ros node
def init():
    global msg, velocity_publisher

    msg = Twist()
    msg.linear.x = 0
    msg.linear.y = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0
    # create ros node
    try:
        
        rospy.init_node('se_youbot', anonymous=True)

        # declare velocity publisher
        cmd_vel_topic = "/cmd_vel"
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        time.sleep(2)
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")

# function to get audio input using microphone as source
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = ""
        try:
            # text = r.recognize_google(audio)
            text = r.recognize_sphinx(audio) # using pocket sphinx instead of google
            print(text)
        except:
            print("Unrecognizeable")
    return text

# make a list of each words and phrasing audio input into string data; return the direction as string value
def phrasing_audio_direction():
    text_lst_direction = ""
    direction = ""
    determine_direction = True

    while determine_direction: 
        print("Give direction input (forward, backward, left, right, stop, exit) :")
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

        elif "counter" in text_lst_direction:
            print("counter")
            direction = "counter"
            determine_direction = False
            return direction  

        elif "clockwise" in text_lst_direction:
            print("clockwise")
            direction = "clockwise"
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

# function to move the robot based on audio input
def move():
        # declare a Twist message to send velocity commands
        msg = Twist()

        global x, y, z, speed

        speed = 0.1 # define the speed of turtle

        direction = "INITIAZION SUCCESS, AWAITING ORDER" # INITIAZION

        loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
        cmd_vel_topic = '/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
        # keep publishing value until new input has been received
        while True :
                rospy.loginfo("youBot move: " + direction)
                velocity_publisher.publish(msg)

                loop_rate.sleep()
                direction = phrasing_audio_direction() # get the direction
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
                    break
        
        # finally, stop the robot after exit
        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.x = 0
        msg.angular.y = 0
        msg.angular.z = 0
                    
        velocity_publisher.publish(msg)

if __name__ == '__main__':

    init()
    move()

