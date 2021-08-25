#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def callback(data):

	text_lst = data.data
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", text_lst)
        if "backward" in text_lst:
            print("Moving Forward")
            msg.linear.x = 0.1
            msg.linear.y = 0
            msg.angular.z = 0
        elif "forward" in text_lst:
            print("Moving Backward")
            msg.linear.x = -0.1
            msg.linear.y = 0
            msg.angular.z = 0
        else:
            print("UNABLE TO RECOGNIZE COMMAND")
            msg.linear.x = 0
            msg.linear.y = 0
            msg.angular.z = 0
        pub.publish(msg)



def listener():
	pub = rospy.Publisher('/vel', Twist, queue_size=10)
	rospy.init_node('drive_listener', anonymous=True)
	rospy.Subscriber("/se_befehl", String, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
