#!/usr/bin/env python


import argparse

import rospy
from colorama import Fore
from std_msgs.msg import String
from pari_aula8_ex4.msg import DogM








def messageReceivedCallback(message):
    #se pusessemos message.name dava o nome do cao enviado
    rospy.loginfo('Received message " ' + Fore.RED + str(message) + Fore.RESET + ' "')

def main():
    parser = argparse.ArgumentParser(description='Optional arguments')

    parser.add_argument('-tn', '--topic_name', help="topic name",
                        action="store",default='chatter')


    args = vars(parser.parse_args())

    #This declares that your node subscribes to the chatter topic which is of type std_msgs.msgs.String.

    rospy.init_node('subscriber', anonymous=True)

    #callback e para chamar a funcao callbac, e o message received
    #so podem passar mensagens do tipo string
    rospy.Subscriber(args['topic_name'], DogM, messageReceivedCallback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()
