#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

import argparse
import cv2

# Global variables
window_name = 'window - Ex3a'
image_gray = None
val = 0


def onTrackbar(threshold):
    # Add code here to threshold image_gray and show image in window
    image_thresholded = cv2.threshold(image_gray, val, 255, cv2.THRESH_BINARY)
    cv2.imshow('image_thresholded', image_thresholded)  # Show the image
    # Add code here to threshold image_gray and show image in window

#def onMouse(event, x, y, flags, param):
 #   if(cv2.ss)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    global image_gray # use global var
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    #cv2.createTrackbar

    # add code to create the trackbar ...
    cv2.waitKey(0)

if __name__ == '__main__':
    main()