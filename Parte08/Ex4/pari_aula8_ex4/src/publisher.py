#! /usr/bin/python


## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic
import argparse

import rospy
from colorama import Fore
from std_msgs.msg import String
from dog_lib import Dog
from pari_aula8_ex4.msg import DogM

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

    pub = rospy.Publisher(args['topic_name'], DogM, queue_size=10)


    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(args['frequency']) # 10hz


    #dog e uma instancia da classe Dog
    #dog = Dog(name='Bobi',age=7,color='Black')

    #agora em vez de criar a instancia mesmo, posso usar a nossa DogM
    #que basicamente e uma instancia da mensagem DogA

    dog_msg = DogM()
    dog_msg.name = 'bobi'
    dog_msg.age = 7
    dog_msg.color = 'black'
    dog_msg.brothers.append('Lassie')



    while not rospy.is_shutdown():

        #log info apenas diz o que vai publicar, nao publica isso, e como fazer print
        rospy.loginfo('Publishing message: "' + Fore.RED + str(dog_msg)+Fore.RESET +
                      '" on topic ' + args['topic_name']  )

        # na realidade a unica coisa a ser enviada e o message content
        pub.publish(dog_msg)
        rate.sleep()
        #The loop calls rate.sleep(), which sleeps just long enough to maintain the desired rate through the loop.

if __name__ == '__main__':
  main()
