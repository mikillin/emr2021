#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback (data):
    global pub
    msg = Twist()
    text_lst = data.data
    rospy.loginfo("Die Nachricht wird bekommen %s", text_lst)
    if "backward" in text_lst:
        print("Moving Backward")
        msg.linear.x = 0.1
        msg.linear.y = 0
        msg.angular.z = 0
    elif "forward" in text_lst:
        print("Moving Forward")
        msg.linear.x = -0.1
        msg.linear.y = 0
        msg.angular.z = 0
    elif "left" in text_lst:
        print("Moving Left")
        msg.linear.x = 0
        msg.linear.y = 0.1
        msg.angular.z = 0
    elif "right" in text_lst:
        print("Moving Right")
        msg.linear.x = 0
        msg.linear.y = -0.1
        msg.angular.z = 0
    elif "stop" in text_lst:
        print("Stop")
        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.z = 0
    else:
        print("UNABLE TO RECOGNIZE COMMAND")
        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.z = 0
    pub.publish(msg)


def listener():
    global pub

    # pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('drive_listener', anonymous=False)
    rospy.Subscriber("/se_befehl", String, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
