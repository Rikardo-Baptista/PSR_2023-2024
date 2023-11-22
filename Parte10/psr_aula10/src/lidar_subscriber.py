#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan

def callbackMessageReceived(data):
    rospy.loginfo('Received laser scan message')
    
def main():
    rospy.init_node('lidar_subscriber', anonymous=False)

    rospy.Subscriber("/left_laser/laserscan", LaserScan, callbackMessageReceived)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()