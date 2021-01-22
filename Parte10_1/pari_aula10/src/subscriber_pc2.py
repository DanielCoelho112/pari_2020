#!/usr/bin/env python


import argparse

import rospy
from colorama import Fore
from std_msgs.msg import String
from sensor_msgs.msg import Image
from pari_aula8_ex4.msg import DogM
import cv2
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String,Header
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import PointCloud2,PointField
from sensor_msgs import point_cloud2


global bridge
global cv_image_depth
global cv_image_rgb
global rgb
global depth
import numpy as np


def message_Depth_ReceivedCallback(message):
    global depth
    global cv_image_depth
    global bridge
    # se pusessemos message.name dava o nome do cao enviado
    depth = True
    #rospy.loginfo('Received message " ' + str(message) + ' "')
    cv_image_depth = bridge.imgmsg_to_cv2(message, desired_encoding='passthrough')


def message_RGB_ReceivedCallback(message):
    global rgb
    global cv_image_rgb
    global bridge
    rgb = True
    # se pusessemos message.name dava o nome do cao enviado
    #rospy.loginfo('Received message " ' + str(message) + ' "')
    cv_image_rgb = bridge.imgmsg_to_cv2(message, "bgr8")


def main():
    global rgb
    global depth
    global cv_image_depth
    global cv_image_rgb
    global bridge
    rgb = False
    depth = False

    cv_image_rgb = np.ones((100, 100, 3), np.uint8) * 255
    cv_image_depth = np.ones((100, 100, 3), np.uint8) * 255

    # This declares that your node subscribes to the chatter topic which is of type std_msgs.msgs.String.

    rospy.init_node('subscriber_RGBD', anonymous=False)
    bridge = CvBridge()

    # callback e para chamar a funcao callbac, e o message received
    # so podem passar mensagens do tipo string

    rospy.Subscriber('/camera/depth/image_raw', Image, message_Depth_ReceivedCallback)
    rospy.Subscriber('/camera/rgb/image_raw', Image, message_RGB_ReceivedCallback)

    #inicializacao do publicador

    '''
    pub = rospy.Publisher('point_cloud_road', PointCloud2, queue_size=10)

    fields = [PointField('x', 0, PointField.FLOAT32, 1),
              PointField('y', 4, PointField.FLOAT32, 1),
              PointField('z', 8, PointField.FLOAT32, 1),
              ]
    header = Header()
    header.frame_id = "left_laser"
    pc2 = point_cloud2.create_cloud(header, fields, cloud_data)
    pc2.header.stamp = rospy.Time.now()
    try:
        pub.publish(pc2)
    except:
        print("Erro a publicar a mensagem")

    '''


    #aqui o objetivo e criar o point cloud2 com as 2 imagens, e envia las para um topico

    while True:

        if rgb == True and depth == True:
            cv2.imshow('rgb', cv_image_rgb)
            cv2.imshow('depth', cv_image_depth)

            b,g,r = cv2.split(cv_image_rgb)
            print(cv_image_rgb.shape)
            print(cv_image_depth.shape)
            d = cv2.split(cv_image_depth)
            #aa=cv2.merge((b, g, r,d))
            #cv2.imshow('aa',aa)
            if chr(cv2.waitKey(1)) == 'q':
                break


if __name__ == '__main__':
    main()
