#!/usr/bin/env python
import rospy
import tf2_ros
import geometry_msgs.msg
import math

if __name__ == '__main__':
    rospy.init_node('body')
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.frame_id = "parent_name"
    t.header.frame_id = rospy.remap_name(t.header.frame_id)
    t.child_frame_id = "child_name"
    t.child_frame_id = rospy.remap_name(t.child_frame_id)

    #as transformacoes sao sempre da child relativamente a header
    distance = rospy.get_param('~distance')
    #distance = 1
    rate = rospy.Rate(10)

    x=0

    while not rospy.is_shutdown():

        if x > 2 * math.pi:
            x = 0

        x += rospy.get_param('~increment')
        #x += 0.001

        t.header.stamp = rospy.Time.now()
        t.transform.translation.x = distance * math.sin(x)
        t.transform.translation.y = distance * math.cos(x)
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        '''
        INVESTIGAR SOBRE QUATERNIONS
        q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]
        '''
        br.sendTransform(t)
        rate.sleep()
