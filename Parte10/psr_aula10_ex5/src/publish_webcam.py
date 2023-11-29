#!/usr/bin/env python3

import rospy

def main():
    rospy.init_node('image_pub')
    rospy.loginfo('image_pub node started')

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass


    