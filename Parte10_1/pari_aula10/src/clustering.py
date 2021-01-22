#!/usr/bin/env python
from random import random

import rospy
from std_msgs.msg import String,Header
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import PointCloud2,PointField
from sensor_msgs import point_cloud2
from visualization_msgs.msg import Marker,MarkerArray
import math
global publisher
global color
global id

#rosbag play lidar_example.bag -l -r 0.9




def messageReceivedCallback(message):
    global pub
    marker_array = MarkerArray()
    global publisher
    global color


    dis_min = 3.0

    angle = message.angle_min



    radius_old=0
    n_cluster=0
    id = 0
    i=0

    for radius in message.ranges:
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        z = 0
        angle += message.angle_increment

        if i==0:
            radius_old=radius


        if radius - radius_old > dis_min:
            n_cluster = n_cluster + 1


        marker = Marker()
        marker.header.frame_id = "/left_laser"
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.ns = 'sphere1'
        marker.scale.x = 0.3
        marker.scale.y = 0.3
        marker.scale.z = 0.3
        marker.color.a = 1
        marker.color.r = color[n_cluster][0]
        marker.color.g = color[n_cluster][1]
        marker.color.b = color[n_cluster][2]
        marker.pose.orientation.w = 1.0
        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 0
        marker.pose.position.x = x
        marker.pose.position.y = y
        marker.pose.position.z = z
        marker_array.markers.append(marker)
        radius_old = radius
        i+=1

    id=0
    for m in marker_array.markers:
        m.id = id
        id += 1
    try:
        publisher.publish(marker_array)
    except:
        pass






def color_cluster():
    color=[]

    for i in range(0,40):
        r = random()
        g = random()
        b = random()
        color.append((r,g,b))
    return color



def main():
    global publisher
    global color


    color = color_cluster()


    topic_name_bag_file = '/left_laser/laserscan'

    rospy.init_node('lidar_subscriber', anonymous=False)
    rospy.Subscriber(topic_name_bag_file, LaserScan, messageReceivedCallback)
    publisher = rospy.Publisher('marker_topic', MarkerArray, queue_size=1000)

    rospy.spin()


if __name__ == '__main__':
    main()
