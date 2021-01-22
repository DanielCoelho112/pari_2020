#! /usr/bin/python


## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic


import rospy
from colorama import Fore
from std_msgs.msg import String
from pari_aula8_ex5.msg import DogM
from pari_aula8_ex5.srv import SetDogName, SetDogNameResponse, SetDogNameRequest

# no que envia informacao e um publisher
# no e um programa em ros


# o publicador e tambem o servidor

global dog_msg


def main():
    global dog_msg

    topic_name = 'chatter'
    pub = rospy.Publisher(topic_name, DogM, queue_size=10)

    # configuracao do servico, handle e a call back function
    s = rospy.Service('set_dog_name', SetDogName, handle_set_dog_name)

    # quando chega um pedido, o programa sai do while e vai a callback function

    rospy.init_node('publisher', anonymous=False)
    rate = rospy.Rate(10)  # 10hz

    # dog e uma instancia da classe Dog
    # dog = Dog(name='Bobi',age=7,color='Black')

    # agora em vez de criar a instancia mesmo, posso usar a nossa DogM
    # que basicamente e uma instancia da mensagem DogA

    dog_msg = DogM()
    dog_msg.name = 'bobi'
    dog_msg.age = 7
    dog_msg.color = 'black'
    dog_msg.brothers.append('Lassie')
    dog_msg.brothers.append('Romeu')



    while not rospy.is_shutdown():
        #~ assume que o parametro esta empurrado no nome
        color = rospy.get_param('~highlight_text_color')
        # log info apenas diz o que vai publicar, nao publica isso, e como fazer print
        rospy.loginfo('Publishing message: \n "' + getattr(Fore,color) + str(dog_msg) + Fore.RESET +
                      '" on topic ' + rospy.remap_name(topic_name))

        # na realidade a unica coisa a ser enviada e o message content
        pub.publish(dog_msg)
        rate.sleep()
        # The loop calls rate.sleep(), which sleeps just long enough to maintain the desired rate through the loop.


# req e o pedido, e como tal, tem la dentro a informacao do new name
def handle_set_dog_name(req):
    global dog_msg
    # get variable new_name from client request
    new_name = req.new_name
    print(Fore.RED + 'Changing dog name from ' + dog_msg.name + 'to' + new_name + Fore.RESET)

    dog_msg.name = new_name

    verify = True

    return SetDogNameResponse(verify)


if __name__ == '__main__':
    main()
