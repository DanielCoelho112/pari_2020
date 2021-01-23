#!/usr/bin/env python
import time
from tf.transformations import euler_from_quaternion
import rospy
import tf2_ros
import geometry_msgs
from geometry_msgs.msg import Twist
import math
import tf_conversions
global br
global t
global pub
from geometry_msgs.msg import PoseStamped
global pose_final
global pose_atual
global orientation
from gazebo_msgs.msg import ModelStates


def reMap(value, maxInput, minInput, maxOutput, minOutput):

	value = maxInput if value > maxInput else value
	value = minInput if value < minInput else value

	inputSpan = maxInput - minInput
	outputSpan = maxOutput - minOutput

	scaledThrust = float(value - minInput) / float(inputSpan)

	return minOutput + (scaledThrust * outputSpan)




def messageReceivedCallback(message):
    global pose_final
    global pose_atual
    global t




    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    rate = rospy.Rate(100)
    while not rospy.is_shutdown():

        # lookup_transform vai buscar a transformada entre os referencias que nos dissermos

        try:
            trans = tfBuffer.lookup_transform("World","p_dcoelho/odom", rospy.Time())
            print('dey')
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue
        # print(trans.transform.translation)
        x = trans.transform.translation.x
        y = trans.transform.translation.y
        break

    #Primeiro tenho de saber a posicao do p_dcoelho em relacao ao world, e depois a que somo estas coordenadas,
    #pois estas coordenadas sao do ponto relativamente ao odom

    #print('Posicao' + str(x) + 'Posicao' + str(y))


    #Aqui sei para onde quero ir!

    message.pose.position.x=message.pose.position.x + x
    message.pose.position.y = message.pose.position.y + y
    pose_final = message.pose
    #print('Para onde vou')
    #print(pose_final)
    t = 1
    find_z_orientation()


def pose_now(message):
    global pose_final
    global pose_atual
    global t
    global q
    q=1

    pose_atual = message.pose[2]
    # print(message.twist)
    # print(Message_Pose)

    #print('Onde estou')
    #print(pose_atual)
    #print(pose_atual.orientation)

    return pose_atual


def find_z_orientation():
    global pose_final
    global pose_atual
    global orientation


    x_f = pose_final.position.x
    x_i = pose_atual.position.x
    y_f = pose_final.position.y
    y_i = pose_atual.position.y

    orientation = math.atan2((y_f-y_i),(x_f-x_i))
    orientation = reMap(orientation,math.pi,-math.pi,1,-1)

    #print(math.degrees(orientation))

    return orientation

def rotate_until_z():
    global pub
    global pose_atual
    global orientation


    print('rotating')
    twist = Twist()
    twist.linear.x = 0.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z =0.2

    pub.publish(twist)


    #print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    #print(orientation)


    while True:

        print("orientacao=" + str(orientation))
        print("Z=" + str(pose_atual.orientation.z))
        (roll,pitch,yaw)=euler_from_quaternion(pose_atual.orientation)
        print("YAW      " + str(yaw))

        time.sleep(0.5)


        '''
        if pose_atual.orientation.z>0.93 * orientation and pose_atual.orientation.z<1.07 * orientation:
            twist = Twist()
            twist.linear.x = 0.0
            twist.linear.y = 0.0
            twist.linear.z = 0.0
            twist.angular.x = 0.0
            twist.angular.y = 0.0
            twist.angular.z = 0.0

            pub.publish(twist)
            #print('ORIENTACAO APONTADAAAAAAAAAAAAAAAAAA')
            break
'''

def straigth_line():
    #print('LINHA DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDIRRRRRRRRRRRRRRRRRRRRRETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    global pub
    twist = Twist()
    twist.linear.x = 0.1
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)









def main():
    global br
    global t
    global pub
    global q
    t=0

    pub = rospy.Publisher('p_dcoelho/cmd_vel', Twist, queue_size=10)

    rospy.init_node('driver', anonymous=False)
    rospy.Subscriber("/move_base_simple/goal", PoseStamped, messageReceivedCallback)
    rospy.Subscriber("/gazebo/model_states", ModelStates, pose_now)


    while True:

        if t==1 and q==1:

            orientation = find_z_orientation()

            rotate_until_z()


            rospy.spin()
                





            print('a')










            rospy.sleep(5)

            straigth_line()

            print('end')
            break








    return
    rospy.spin()

    #pub = rospy.Publisher('p_dcoelho/cmd_vel', Twist, queue_size=10)
    #rate = rospy.Rate(50)  # 10hz
    '''
    try:

        while not rospy.is_shutdown():

            twist = Twist()
            twist.linear.x = 1.0
            twist.linear.y = 0.0
            twist.linear.z = 0.0
            twist.angular.x = 0.0
            twist.angular.y = 0.0
            twist.angular.z = -1.0

            pub.publish(twist)

            rate.sleep()


    except:

            twist = Twist()
            twist.linear.x = 0.0
            twist.linear.y = 0.0
            twist.linear.z = 0.0
            twist.angular.x = 0.0
            twist.angular.y = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)

    '''

if __name__ == '__main__':
    main()
