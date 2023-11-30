#!/usr/bin/env python3

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import rospy
import cv2

def main():
    #--------------------------
    # Initialization
    #--------------------------

    rospy.init_node('image_publisher', anonymous=False)

    publisher = rospy.Publisher('~image', Image, queue_size=1)

    capture = cv2.VideoCapture(0)
    window_name = 'window'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    rate = rospy.Rate(15)
   
    #--------------------------
    # Execution
    #--------------------------
    while True:
        _, image = capture.read()  # get an image from the camera

    #--------------------------
    # Visualization
    #--------------------------
        cv2.imshow('window', image)  # Display the image
        
        bridge = CvBridge()
        image_message = bridge.cv2_to_imgmsg(image, encoding='bgr8')
        publisher.publish(image_message)

        if cv2.waitKey(1) == ord('q'):
            break

        rate.sleep()

    capture.release()
    cv2.destroyAllWindows()

    rospy.spin()
    
if __name__ == '__main__':
    main()

    