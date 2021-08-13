#! /usr/bin/python
#import random
from random import random

import rospy
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import math


def main():
    # ---------------
    # initial setup
    # ---------------

    rospy.init_node('marker_publisher', anonymous=False)
    publisher = rospy.Publisher('Marker_topic', MarkerArray, queue_size=100)
    rate = rospy.Rate(10)  # 10hz


    # ---------------
    # program's body
    # ---------------

    while not rospy.is_shutdown():

        marker_array = MarkerArray()




        for id in range(0,100):

            x = random() *  10
            y =random() * 10
            z = random() * 10



            # SPHERE
            marker = Marker()
            marker.header.stamp = rospy.Time.now()
            marker.header.frame_id = "/map"
            marker.type = marker.SPHERE
            marker.action = marker.ADD
            marker.id = id
            marker.ns = 'sphere'
            marker.scale.x = 1
            marker.scale.y = 1
            marker.scale.z = 1
            marker.color.a = 0.5
            marker.color.r = 0
            marker.color.g = 1
            marker.color.b = 0
            marker.pose.orientation.w = 1.0
            marker.pose.orientation.x = 0
            marker.pose.orientation.y = 0
            marker.pose.orientation.z = 0
            marker.pose.position.x = x
            marker.pose.position.y = y
            marker.pose.position.z = z



            # CUBE
            marker_cube = Marker()
            marker_cube.header.stamp = rospy.Time.now()
            marker_cube.header.frame_id = "/map"
            marker_cube.ns = 'cube'
            marker_cube.type = marker.CUBE
            marker_cube.action = marker.ADD
            marker_cube.id = id
            marker_cube.scale.x = 0.5
            marker_cube.scale.y = 0.5
            marker_cube.scale.z = 0.5
            marker_cube.color.a = 1
            marker_cube.color.r = 1
            marker_cube.color.g = 0
            marker_cube.color.b = 0
            marker_cube.pose.orientation.w = 1.0
            marker_cube.pose.orientation.x = 0
            marker_cube.pose.orientation.y = 0
            marker_cube.pose.orientation.z = 0
            marker_cube.pose.position.x = x
            marker_cube.pose.position.y = y
            marker_cube.pose.position.z = z

            # TEXT

            marker_text = Marker()
            marker_text.header.stamp = rospy.Time.now()
            marker_text.header.frame_id = "/map"
            marker_text.id = id
            marker_text.ns = 'text'
            marker_text.type = marker.TEXT_VIEW_FACING
            marker_text.text = 'Raio: 1'
            marker_text.action = marker.ADD
            marker_text.scale.z = 0.5
            marker_text.color.a = 1
            marker_text.color.r = 0
            marker_text.color.g = 0
            marker_text.color.b = 0
            marker_text.pose.orientation.w = 1.0
            marker_text.pose.orientation.x = 0
            marker_text.pose.orientation.y = 0
            marker_text.pose.orientation.z = 0
            marker_text.pose.position.x = x
            marker_text.pose.position.y = y
            marker_text.pose.position.z = z


            marker_array.markers.append(marker)
            marker_array.markers.append(marker_cube)
            marker_array.markers.append(marker_text)

            #publisher.publish(marker)
            #publisher.publish(marker_cube)
            #publisher.publish(marker_text)

        publisher.publish(marker_array)
        rospy.sleep(1)

    # ---------------
    # program's end
    # ---------------


if __name__ == '__main__':
    main()
