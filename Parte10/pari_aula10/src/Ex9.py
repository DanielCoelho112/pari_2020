#!/usr/bin/env python


import rospy
from std_msgs.msg import String,Header
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import PointCloud2,PointField
from sensor_msgs import point_cloud2
from visualization_msgs.msg import Marker,MarkerArray
import math
global publisher
global Array_Near
global Array_Medium
global Array_Far
global MARKERS_MAX_NEAR
global MARKERS_MAX_MEDIUM
global MARKERS_MAX_FAR



def messageReceivedCallback(message):
    global pub
    global Array_Near
    global Array_Medium
    global Array_Far
    global MARKERS_MAX_NEAR
    global MARKERS_MAX_MEDIUM
    global MARKERS_MAX_FAR
    Array_Near = MarkerArray()
    Array_Medium = MarkerArray()
    Array_Far = MarkerArray()
    global publisher

    angle = message.angle_min
    #List that will contain all [x,y,z] coordinates
    cloud_data_near = []
    cloud_data_medium = []
    cloud_data_far = []

    for radius in message.ranges:
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        z = 0
        point = (x,y,z)

        if radius > 0 and radius < 5:
            cloud_data_near.append(point)
        elif radius > 5 and radius < 10:
            cloud_data_medium.append(point)
        else:
            cloud_data_far.append(point)

        angle += message.angle_increment

    count_near=0
    count_medium=0
    count_far=0
    for i in range(0,len(cloud_data_near)):
        marker = Marker()
        marker.header.stamp = rospy.Time.now()
        marker.header.frame_id = "/left_laser"
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.ns = 'sphere_near'
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 0.5
        marker.color.r = 0
        marker.color.g = 1
        marker.color.b = 0
        marker.pose.orientation.w = 1.0
        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 0
        marker.pose.position.x = cloud_data_near[i][0]
        marker.pose.position.y = cloud_data_near[i][1]
        marker.pose.position.z = cloud_data_near[i][2]

        if (count_near > MARKERS_MAX_NEAR):
            #Array_Near.markers.pop(0)
            Array_Near=MarkerArray()


        Array_Near.markers.append(marker)
        id = 0
        for m in Array_Near.markers:
            m.id = id

            id += 1
        #publisher.publish(marker)
        publisher.publish(Array_Near)
        count_near+=1


    for i in range(0,len(cloud_data_medium)):
        marker = Marker()
        marker.header.stamp = rospy.Time.now()
        marker.header.frame_id = "/left_laser"
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.ns = 'sphere_medium'
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 0.5
        marker.color.r = 0
        marker.color.g = 0
        marker.color.b = 1
        marker.pose.orientation.w = 1.0
        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 0
        marker.pose.position.x = cloud_data_medium[i][0]
        marker.pose.position.y = cloud_data_medium[i][1]
        marker.pose.position.z = cloud_data_medium[i][2]

        if (count_medium > MARKERS_MAX_MEDIUM):
            Array_Medium.markers.pop(0)


        Array_Medium.markers.append(marker)
        id = 0
        for m in Array_Medium.markers:
            m.id = id

            id += 1
        #publisher.publish(marker)
        publisher.publish(Array_Medium)
        count_medium += 1

    for i in range(0,len(cloud_data_far)):
        marker = Marker()
        marker.header.stamp = rospy.Time.now()
        marker.header.frame_id = "/left_laser"
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.ns = 'sphere_far'
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 0.5
        marker.color.r = 1
        marker.color.g = 0
        marker.color.b = 0
        marker.pose.orientation.w = 1.0
        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 0
        marker.pose.position.x = cloud_data_far[i][0]
        marker.pose.position.y = cloud_data_far[i][1]
        marker.pose.position.z = cloud_data_far[i][2]

        if (count_far > MARKERS_MAX_FAR):
            Array_Far.markers.pop(0)

        Array_Far.markers.append(marker)

        #publisher.publish(marker)
        publisher.publish(Array_Far)
        count_far += 1





def main():
    global publisher
    global Array_Near
    global MARKERS_MAX_NEAR
    global MARKERS_MAX_MEDIUM
    global MARKERS_MAX_FAR

    MARKERS_MAX_NEAR=700
    MARKERS_MAX_MEDIUM=700
    MARKERS_MAX_FAR = 700


    Array_Near = MarkerArray()

    topic_name_bag_file = 'left_laser/laserscan'

    rospy.init_node('lidar_subscriber', anonymous=False)
    rospy.Subscriber(topic_name_bag_file, LaserScan, messageReceivedCallback)
    publisher = rospy.Publisher('Marker_topic', MarkerArray, queue_size=100)
    rate = rospy.Rate(10)  # 10hz

    rospy.spin()


if __name__ == '__main__':
    main()
