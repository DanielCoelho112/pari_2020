#!/usr/bin/env python
"""
Practical work 3 (PARI Team Hunt): driver.py
Group 3:
Ruben Almeida 72648
Miguel Pina 80203
Last revisited: January 21st, 2021
"""
# Imports
import rospy
from sensor_msgs.msg import Image, LaserScan
from geometry_msgs.msg import Twist
from functools import partial
import cv2
from cv_bridge import CvBridge
import numpy as np
from colorama import Fore
from pprint import pprint
from gazebo_msgs.msg import ContactsState

# Global dictionary to determine the robot next move
MovementInputs = {
  "unwanted_collision": False,
  "wall_in_front_left": False,
  "wall_in_front_right": False,
  "hunter_in_image": False,
  "hunter_position": None,
  "prey_in_image": False,
  "prey_position": None
}


def CollisionCallback(collision_msg, prey, hunter, my_team):
    """
    __& CollisionCallback FUNCTION &__
    This function is called everytime there is data subscribed to /<player_name>/contact
    :return: void
    """
    global MovementInputs

    # Executes this code if it collides with another robot/object
    if collision_msg.states:
        # Strings with both robots/objects that collided
        coll_1 = collision_msg.states[0].collision1_name
        coll_2 = collision_msg.states[0].collision2_name

        # Conditions to see the collision that happened
        same_robot_collision = (my_team in coll_1) and (my_team in coll_2)

        robot_hunt_prey = ((my_team in coll_1) and (prey in coll_2)) or \
                          ((my_team in coll_2) and (prey in coll_1))

        hunter_caught_robot = ((my_team in coll_1) and (hunter in coll_2)) or \
                              ((my_team in coll_2) and (hunter in coll_1))
        if hunter_caught_robot or robot_hunt_prey:
            MovementInputs["unwanted_collision"] = False
        else:
            MovementInputs["unwanted_collision"] = True


def LaserScanCallback(lasermsg):
    global MovementInputs

    # Create clusters of points
    threshold_max_range_difference = 0.5  # in meters
    cluster_idx = 0
    points_cluster = []
    front_ranges = list(lasermsg.ranges[270:360])
    front_ranges.extend(list(lasermsg.ranges[0:90]))

    for idx, msg_range in enumerate(front_ranges):
        # print str(idx) + 'degrees --> ' + str(msg_range)
        # print '0 degrees --> ' + str(lasermsg.ranges[0])
        # print front_ranges[len(front_ranges)/2]

        if abs(msg_range - front_ranges[idx - 1]) > threshold_max_range_difference and idx != 0:
            cluster_idx += 1
        points_cluster.append(cluster_idx)

    # print points_cluster
    # print points_cluster[len(points_cluster)/2]

    cluster_in_front = points_cluster[len(points_cluster)/2]

    front_right_cluster = points_cluster[0:len(front_ranges) / 2]
    front_right_cluster = front_right_cluster.count(cluster_in_front)

    front_left_cluster = points_cluster[len(front_ranges) / 2:len(front_ranges)]
    front_left_cluster = front_left_cluster.count(cluster_in_front)

    print points_cluster.count(cluster_in_front)
    print front_ranges[len(front_ranges) / 2]

    dist_to_wall = min(front_ranges[len(front_ranges)/2 - len(front_ranges)/15:len(front_ranges)/2 + len(front_ranges)/15])
    print dist_to_wall

    if dist_to_wall < 1.0 and points_cluster.count(cluster_in_front) > 75:
        if front_right_cluster > front_left_cluster:
            MovementInputs["wall_in_front_right"] = True
            MovementInputs["wall_in_front_left"] = False
        else:
            MovementInputs["wall_in_front_left"] = True
            MovementInputs["wall_in_front_right"] = False
    else:
        MovementInputs["wall_in_front_right"] = False
        MovementInputs["wall_in_front_left"] = False


def BiggestBlobCenter(mask):
    """
    Function that takes the mask of the image and returns the biggest blob and the center of that blob
    """
    mask_largest = np.zeros(mask.shape, np.uint8)
    _, cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cnt = max(cnts, key=cv2.contourArea)
    cv2.drawContours(mask_largest, [cnt], -1, 255, cv2.FILLED)
    mask_largest = cv2.bitwise_and(mask, mask_largest)

    # Calculates moments of the binary image
    M = cv2.moments(mask_largest)

    # Calculates x,y coordinate of center
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])

    return mask_largest, cx, cy


def ImageCallback(image_received, my_team):
    """
    __& ImageCallback FUNCTION &__
    This function is called everytime there is data subscribed to /<player_name>/camera/rgb/image_raw
    :return: void
    """
    global MovementInputs

    # Initialize the CvBridge class
    bridge = CvBridge()

    # Try to convert the ROS Image message to a CV2 Image
    try:
        cv_image = bridge.imgmsg_to_cv2(image_received, desired_encoding='bgr8')
        image_hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

        # Define the limits arrays
        green_lower_limits = np.array([40, 100, 100])
        green_higher_limits = np.array([80, 255, 255])

        blue_lower_limits = np.array([116, 180, 100])
        blue_higher_limits = np.array([124, 255, 150])

        red_lower_limits1 = np.array([0, 50, 50])
        red_higher_limits1 = np.array([4, 255, 255])
        red_lower_limits2 = np.array([175, 50, 50])
        red_higher_limits2 = np.array([180, 255, 255])

        prey_mask = np.zeros(image_hsv.shape, np.uint8)
        hunter_mask = np.zeros(image_hsv.shape, np.uint8)

        if 'green' in my_team:

            prey_mask = cv2.inRange(image_hsv, blue_lower_limits, blue_higher_limits)
            hunter_mask1 = cv2.inRange(image_hsv, red_lower_limits1, red_higher_limits1)
            hunter_mask2 = cv2.inRange(image_hsv, red_lower_limits2, red_higher_limits2)
            hunter_mask = hunter_mask1 | hunter_mask2

        elif 'blue' in my_team:

            prey_mask1 = cv2.inRange(image_hsv, red_lower_limits1, red_higher_limits1)
            prey_mask2 = cv2.inRange(image_hsv, red_lower_limits2, red_higher_limits2)
            prey_mask = prey_mask1 | prey_mask2
            hunter_mask = cv2.inRange(image_hsv, green_lower_limits, green_higher_limits)

        elif 'red' in my_team:

            prey_mask = cv2.inRange(image_hsv, green_lower_limits, green_higher_limits)
            hunter_mask = cv2.inRange(image_hsv, blue_lower_limits, blue_higher_limits)

        # ----------------------
        # Code for hunting preys
        # ----------------------
        if cv2.countNonZero(prey_mask) == 0:
            MovementInputs["prey_in_image"] = False
            MovementInputs["hunter_position"] = None
            MovementInputs["prey_position"] = None
        else:
            MovementInputs["prey_in_image"] = True

            (prey_mask, x, y) = BiggestBlobCenter(prey_mask)

            imageWidth = prey_mask.shape[1]
            distance_x = x - imageWidth / 2

            if -4 <= distance_x <= 4:
                MovementInputs["prey_position"] = "Front"
            elif distance_x < -4:
                MovementInputs["prey_position"] = "Left"
            else:
                MovementInputs["prey_position"] = "Right"

        # -----------------------------
        # Code for running from hunters
        # -----------------------------
        if cv2.countNonZero(hunter_mask) == 0:
            MovementInputs["hunter_in_image"] = False
        else:
            MovementInputs["hunter_in_image"] = True

            (hunter_mask, x, y) = BiggestBlobCenter(hunter_mask)

            imageWidth = hunter_mask.shape[1]
            distance_x = x - imageWidth / 2

            if -4 <= distance_x <= 4:
                MovementInputs["hunter_position"] = "Front"
            elif distance_x <= -4:
                MovementInputs["hunter_position"] = "Left"
            else:
                MovementInputs["hunter_position"] = "Right"
    except:
        pass


def main():
    """
    This is the main function of the file.
    :return: void
    """
    global MovementInputs

    # Initialize the ros node
    rospy.init_node('driver', anonymous=False)
    node_name = rospy.get_name().strip('/')

    velocity_message = Twist()

    # Get a global parameter for each player_color
    red_names = rospy.get_param('/red_players')
    green_names = rospy.get_param('/green_players')
    blue_names = rospy.get_param('/blue_players')

    my_team = prey_team_players = hunter_team_players = prey_color = hunter_color = None

    if node_name in red_names:
        my_team = 'red'
        prey_color = 'green'
        hunter_color = 'blue'
        prey_team_players = green_names
        hunter_team_players = blue_names
    elif node_name in green_names:
        my_team = 'green'
        prey_color = 'blue'
        hunter_color = 'red'
        prey_team_players = blue_names
        hunter_team_players = red_names
    elif node_name in blue_names:
        my_team = 'blue'
        prey_color = 'red'
        hunter_color = 'green'
        prey_team_players = red_names
        hunter_team_players = green_names
    else:
        rospy.logerr('Something is wrong')
        exit(0)

    color_preys = getattr(Fore, prey_color.upper())
    color_hunters = getattr(Fore, hunter_color.upper())
    color_teammates = getattr(Fore, my_team.upper())

    print('My name is ' + color_teammates + node_name + Fore.RESET + '. I am team ' + color_teammates +
          my_team + Fore.RESET + '. I am hunting ' + color_preys + str(prey_team_players) + Fore.RESET +
          '. I am fleeing from ' + color_hunters + str(hunter_team_players) + Fore.RESET)

    player_name = node_name

    # Setup the publisher to the desired topic name and defines the rate (Hz) of publishing
    topic_name = player_name + '/cmd_vel'
    publisher = rospy.Publisher(topic_name, Twist, queue_size=10)
    rate = rospy.Rate(4)  # 4hz

    # Initialize a subscriber to the "/camera/rgb/image_raw" topic with the function "image_callback" as a callback
    sub_image = rospy.Subscriber("/" + player_name + "/camera/rgb/image_raw",
                                 Image,
                                 partial(ImageCallback, my_team=my_team))

    sub_collisions = rospy.Subscriber("/" + player_name + "/contact",
                                      ContactsState,
                                      partial(CollisionCallback,
                                              prey=prey_color,
                                              hunter=hunter_color,
                                              my_team=my_team))

    sub_laserscan = rospy.Subscriber("/" + player_name + '/scan',
                                     LaserScan,
                                     LaserScanCallback)

    # Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
    while not rospy.is_shutdown():
        try:
            if MovementInputs["unwanted_collision"]:
                velocity_message.linear.x = -0.5
                velocity_message.angular.z = 0.0
            else:
                if MovementInputs["wall_in_front_left"]:
                    velocity_message.linear.x = 0.2
                    velocity_message.angular.z = -2.0
                elif MovementInputs["wall_in_front_right"]:
                    velocity_message.linear.x = 0.2
                    velocity_message.angular.z = 2.0
                else:
                    if not MovementInputs["hunter_in_image"] and not MovementInputs["prey_in_image"]:
                        velocity_message.linear.x = 1.0
                        velocity_message.angular.z = 0.0
                    elif not MovementInputs["hunter_in_image"] and MovementInputs["prey_in_image"]:
                        if MovementInputs["prey_position"] == "Front":
                            velocity_message.linear.x = 1.0
                            velocity_message.angular.z = 0.0
                        elif MovementInputs["prey_position"] == "Right":
                            velocity_message.linear.x = 1.0
                            velocity_message.angular.z = -0.75
                        elif MovementInputs["prey_position"] == "Left":
                            velocity_message.linear.x = 1.0
                            velocity_message.angular.z = 0.75
                        else:
                            velocity_message.linear.x = 1.0
                            velocity_message.angular.z = 0.0
                    elif MovementInputs["hunter_in_image"]:
                        if MovementInputs["hunter_position"] == "Front":
                            velocity_message.linear.x = 1.0
                            velocity_message.angular.z = 0.0
                        elif MovementInputs["hunter_position"] == "Right":
                            velocity_message.linear.x = 1.0
                            velocity_message.angular.z = 0.75
                        elif MovementInputs["hunter_position"] == "Left":
                            velocity_message.linear.x = 1.0
                            velocity_message.angular.z = -0.75
                        else:
                            velocity_message.linear.x = 1.0
                            velocity_message.angular.z = 0.0

            pprint(MovementInputs)
            MovementInputs["unwanted_collision"] = False
            publisher.publish(velocity_message)
            rate.sleep()
        except:
            pass


if __name__ == '__main__':
    main()
