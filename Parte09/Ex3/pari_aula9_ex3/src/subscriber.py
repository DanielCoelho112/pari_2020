#!/usr/bin/env python


import argparse

import rospy
from colorama import Fore
from std_msgs.msg import String
from pari_aula8_ex4.msg import DogM


highlight_text_color = 'RED'

def messageReceivedCallback(message):
    #se pusessemos message.name dava o nome do cao enviado
    global highlight_text_color
    highlight_text_color = rospy.get_param("~highlight_text_color")
    rospy.loginfo('Received message " ' + getattr(Fore,highlight_text_color) + str(message) + Fore.RESET + ' "')

def main():

    topic_name = 'chatter'


    #This declares that your node subscribes to the chatter topic which is of type std_msgs.msgs.String.

    rospy.init_node('subscriber', anonymous=False)

    global highlight_text_color

    highlight_text_color = rospy.get_param("~highlight_text_color")



    #callback e para chamar a funcao callbac, e o message received
    #so podem passar mensagens do tipo string
    rospy.Subscriber(topic_name, DogM, messageReceivedCallback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()
