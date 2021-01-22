#! /usr/bin/python







# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic
import argparse

import rospy
from colorama import Fore
from std_msgs.msg import String

#no que envia informacao e um publisher
# no e um programa em ros


#criar packges sempre onde esta o gennigers tuturials










def main():
    parser = argparse.ArgumentParser(description='Optional arguments')

    parser.add_argument('-tn', '--topic_name',default='chatter', help="topic name",
                        action="store")

    parser.add_argument('-m', '--message_content',default='nothing to say' ,help="message",
                        action="store")
    parser.add_argument('-f', '--frequency',type=float,default=10 ,help='freq', action="store")

    args = vars(parser.parse_args())


    #) declares that your node is publishing to the chatter topic using the message type String


    #criacao de um publicador
    pub = rospy.Publisher(args['topic_name'], String, queue_size=10)

    #tells rospy the name of your node
    #anonymous = True ensures that your node has a unique name by adding random numbers to the end of NAME
    #publisher e o nome do no

    #inicializacao do meu no
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(args['frequency']) # 10hz

    #este ciclo corre a 10hz devido ao sleep
    #podemos enviar strings, imagens, estruturas de dados avancadas...
    while not rospy.is_shutdown():

        #log info apenas diz o que vai publicar, nao publica isso, e como fazer print
        rospy.loginfo('Publishing message: "' + Fore.RED + args['message_content']+Fore.RESET +
                      '" on topic ' + args['topic_name']  )

        # na realidade a unica coisa a ser enviada e o message content
        pub.publish(args['message_content'])
        rate.sleep()
        #The loop calls rate.sleep(), which sleeps just long enough to maintain the desired rate through the loop.

if __name__ == '__main__':
  main()
