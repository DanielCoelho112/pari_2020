#!/usr/bin/env python


import rospy
from gazebo_msgs.msg import ModelStates
import tf2_ros
import geometry_msgs.msg
import math
import tf_conversions

global br
global t



global pub



def messageReceivedCallback(message):
    global br
    global t
    Childs=message.name
    Message_Pose=message.pose
    #print(message.twist)
    #print(Message_Pose)
    print(Childs)
    print(Message_Pose)


    #Parte de envio

    if len(Childs)>2:


        for index in range(2,len(Childs)):

            try:
                t.header.frame_id = "World"

                child_name = Childs[index] + "/odom"
                #t.child_frame_id = "p_dcoelho/base_footprint"
                t.child_frame_id = child_name

                t.header.stamp = rospy.Time.now()
                t.transform.translation.x = Message_Pose[index].position.x
                t.transform.translation.y = Message_Pose[index].position.y
                t.transform.translation.z = Message_Pose[index].position.z
                t.transform.rotation.x = Message_Pose[index].orientation.x
                t.transform.rotation.y = Message_Pose[index].orientation.y
                t.transform.rotation.z = Message_Pose[index].orientation.z
                t.transform.rotation.w = Message_Pose[index].orientation.w
                br.sendTransform(t)
            except:
                pass







def main():
    global br
    global t
    pub=0

    rospy.init_node('model_states_to_tf', anonymous=False)
    rospy.Subscriber("/gazebo/model_states",ModelStates, messageReceivedCallback)
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()


    rospy.spin()


if __name__ == '__main__':
    main()
