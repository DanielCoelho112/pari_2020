#!/usr/bin/env python
import rospy
from std_msgs.msg import String
rospy.init_node("test_node",xmlrpc_port=20000, tcpros_port=10000)
pub = rospy.Publisher("daniel", String, queue_size=1)
msg = String()
msg.data = "olasasjkdaskjd"
r = rospy.Rate(50)
while not rospy.is_shutdown():
    print(msg)
    pub.publish(msg)
