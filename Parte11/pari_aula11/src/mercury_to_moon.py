#!/usr/bin/env python
import rospy

import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('tf2_listener')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():


        #lookup_transform vai buscar a transformada entre os referencias que nos dissermos

        try:
            trans = tfBuffer.lookup_transform('Mercurio', 'Lua', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue
        #print(trans.transform.translation)
        x = trans.transform.translation.x
        y = trans.transform.translation.y
        dist = (x**2 + y**2)**(0.5)
        print('Distancia Mercurio Lua: ' + str(dist))

    ##DUVIDA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #depois com a trans, consigo saber a distancia e os pontos
