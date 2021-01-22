#!/usr/bin/env python
from random import random

import rospy
from std_msgs.msg import String,Header
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import PointCloud2,PointField
from sensor_msgs import point_cloud2
from visualization_msgs.msg import Marker,MarkerArray
import matplotlib
from matplotlib import cm
from matplotlib.pyplot import viridis


colormap = cm.gist_rainbow(range(0,100))
print(colormap)
exit(0)
import math
global publisher
global color
global id

#rosbag play lidar_example.bag -l -r 0.9


def messageReceivedCallback(message):
    # type: (object) -> object
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
    marker = Marker(header=Header(frame_id=message.frame_id, stamp=message.header.stamp), ns='Clusters', id=0,
                    type=Marker.POINTS, action=Marker.ADD)

    marker.scale.x = 0.3
    marker.scale.y = 0.3
    marker.scale.z = 0.3
    marker.color.a = 1
    marker.pose.orientation.w = 1.0

    treshold_max_range = 0.5

    for idx,radius in enumerate(message.ranges):

        if idx==0:
            continue

        if abs(radius - message.ranges[idx-1]) > treshold_max_range:
            pass

        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        z = 0
        angle += message.angle_increment

        point = Point(x=x,y=y,z=0)
        marker.points.append(point)

        color = ColorRGBA(r=1,g=0,b=0)
        marker.colors.append(color)

        marker_array = MarkerArray()
        marker_array.markers.append(marker)
        publisher.pub(marker_array)

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

    return None






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
