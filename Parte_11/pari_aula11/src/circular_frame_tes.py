#!/usr/bin/env python
import rospy
import tf2_ros
import geometry_msgs.msg
import math
import tf_conversions

if __name__ == '__main__':
    rospy.init_node('body')
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.frame_id = "parent_name"
    #t.header.frame_id = rospy.remap_name(t.header.frame_id)
    t.child_frame_id = "child_name"
    #t.child_frame_id = rospy.remap_name(t.child_frame_id)

    #as transformacoes sao sempre da child relativamente a header
    distance = 1
    #distance = 1
    rate = rospy.Rate(10)

    x=0

    while not rospy.is_shutdown():

        if x > 2 * math.pi:
            x = 0


        x += 0.01

        t.header.stamp = rospy.Time.now()
        t.transform.translation.x = 1
        t.transform.translation.y = 1
        t.transform.translation.z = 0.0

        #INVESTIGAR SOBRE QUATERNIONS

        q = tf_conversions.transformations.quaternion_from_euler(0, 0, x)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        '''
        Neste caso fizemos a translacao e uma rotacao, ele primeiro efetua a translacao e depois efetua a rotacao,
        a rotacao e relativamente ao novo referencial, dai rodar sobre ele    
        Ate e ao contrario, primeiro efetua a rotacao e so depois a translacao
        '''


        br.sendTransform(t)
        rate.sleep()
