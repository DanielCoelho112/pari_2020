#! /usr/bin/python
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def main():
    # ---------------
    # initial setup
    # ---------------
    window_name = 'OpenCV'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    capture = cv2.VideoCapture(0)  # 0 is the camara's index
    bridge = CvBridge()
    rospy.init_node('image_publisher', anonymous=False)
    pub = rospy.Publisher('Images', Image, queue_size=10)
    rate = rospy.Rate(10)  # 10hz

    # ---------------
    # program's body
    # ---------------
    while not rospy.is_shutdown():
        _, image = capture.read()
        cv2.imshow(window_name, image)
        image_message = bridge.cv2_to_imgmsg(image, "bgr8")
        pub.publish(image_message)
        if chr(cv2.waitKey(1)) == 'q':
            break
        rate.sleep()

    # ---------------
    # program's end
    # ---------------
    cv2.destroyAllWindows()
    capture.release()


if __name__ == '__main__':
    main()
