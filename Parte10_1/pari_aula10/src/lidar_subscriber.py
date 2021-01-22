#!/usr/bin/env python


import rospy
from std_msgs.msg import String,Header
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import PointCloud2,PointField
from sensor_msgs import point_cloud2
import math
global pub


def messageReceivedCallback(message):
    global pub

    angle = message.angle_min
    #List that will contain all [x,y,z] coordinates
    cloud_data = []

    for radius in message.ranges:
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        z = 0
        point = [x,y,z]
        cloud_data.append(point)
        angle += message.angle_increment


    #0,4,8 is the offset
    #x,y,z have 4 bytes each (float32)
    fields = [PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 4, PointField.FLOAT32, 1),
          PointField('z', 8, PointField.FLOAT32, 1),
          ]
    header = Header()
    header.frame_id = message.header.frame_id
    pc2 = point_cloud2.create_cloud(header,fields,cloud_data)
    pc2.header.stamp = rospy.Time.now()
    try:
        pub.publish(pc2)
    except:
        print("Erro a publicar a mensagem")



def main():
    global pub

    topic_name_bag_file = 'left_laser/laserscan'

    rospy.init_node('lidar_subscriber', anonymous=False)
    rospy.Subscriber(topic_name_bag_file, LaserScan, messageReceivedCallback)
    pub = rospy.Publisher('point_cloud_road', PointCloud2, queue_size=10)

    rospy.spin()


if __name__ == '__main__':
    main()
