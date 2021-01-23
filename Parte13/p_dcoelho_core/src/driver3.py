#!/usr/bin/env python
import time
from tf.transformations import euler_from_quaternion
import rospy
import tf2_ros
import geometry_msgs
from geometry_msgs.msg import Twist
import math
import tf_conversions
from geometry_msgs.msg import PoseStamped
from gazebo_msgs.msg import ModelStates



global br
global t
global pub
global posicao_final
global posicao_atual
global orientation
global new_goal



def read_goal(message):
    global pose_final
    global pose_atual
    global t
    global new_goal


    new_goal=1

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    rate = rospy.Rate(100)
    while not rospy.is_shutdown():

        # lookup_transform vai buscar a transformada entre os referencias que nos dissermos

        try:
            trans = tfBuffer.lookup_transform("World","p_dcoelho/odom", rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue
        # print(trans.transform.translation)
        x1 = trans.transform.translation.x
        y1 = trans.transform.translation.y
        break

    #Primeiro tenho de saber a posicao do p_dcoelho em relacao ao world, e depois a que somo estas coordenadas,
    #pois estas coordenadas sao do ponto relativamente ao odom

    #print('Posicao' + str(x) + 'Posicao' + str(y))


    #Aqui sei para onde quero ir!

    #message.pose.position.x=message.pose.position.x + x1
    #message.pose.position.y = message.pose.position.y + y1
    pose_final = message.pose
    t = 1

def my_position(message):
    global pose_final
    global pose_atual
    global t
    global q
    global x
    global y
    global theta
    global new_goal

    #Tenho de ler apenas o posicao do meu robot

    names = message.name
    index=0
    index_name=None
    for name in names:
        if name=="p_dcoelho":
            index_name=index
            break
        index+=1



    x = message.pose[index_name].position.x
    y = message.pose[index_name].position.y

    rot_q = message.pose[index_name].orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
    q=1



def aim_to_goal():
    global pub
    global pose_atual
    global pose_final
    global orientation
    global new_goal
    twist = Twist()
    finish=0
    twist.linear.x = 0.0
    twist.angular.z = 0.4

    while not rospy.is_shutdown():
        inc_x = pose_final.position.x - x
        inc_y = pose_final.position.y - y

        print('atual' + str(theta))



        angle_to_goal = math.atan2(inc_y, inc_x)
        print('final' + str(angle_to_goal))

        if abs(angle_to_goal - theta) > 0.5:

            twist.linear.x = 0.0



            twist.angular.z = (angle_to_goal-theta)/2


        else:
            if (math.sqrt(inc_y**2+inc_x**2)/2)>4:

                twist.linear.x = 3
                twist.angular.z = 0.0

            else:
                twist.linear.x = math.sqrt(inc_y**2+inc_x**2)
                twist.angular.z = 0.0



        if math.sqrt(inc_y**2+inc_x**2)<0.1:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            print('CHEGOU')


        pub.publish(twist)
        rospy.sleep(0.01)





        if finish==1:
            new_goal=0
            break



def straigth_line():
    global pub
    global pub
    global pose_atual
    global pose_final
    global orientation
    global new_goal
    twist = Twist()
    finish = 0

    while not rospy.is_shutdown():

        inc_x = pose_final.position.x - x
        inc_y = pose_final.position.y - y

        distancia=math.sqrt(inc_y**2+inc_x**2)

        twist.linear.x = math.sqrt(distancia)
        twist.angular.z = 0.0

        pub.publish(twist)

        if new_goal==1:
            print('erro')
            aim_to_goal()



        if distancia<0.1:
            twist.linear.x = 0.0
            twist.angular.z = 0.0


            break










def main():
    global br
    global t
    global pub
    global q
    t=0

    pub = rospy.Publisher('p_dcoelho/cmd_vel', Twist, queue_size=10)

    rospy.init_node('driver', anonymous=False)
    rospy.Subscriber("/move_base_simple/goal", PoseStamped, read_goal)
    rospy.Subscriber("/gazebo/model_states", ModelStates, my_position)


    while not rospy.is_shutdown():

        if t==1 and q==1:

            aim_to_goal()


            #straigth line tem de ter codigo para parar, fazer velocidade com base na distancia



            print('end')





if __name__ == '__main__':
    main()
