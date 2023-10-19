#!/usr/bin/env python3
import cv2

def main():
    #--------------------------
    # Initialization
    #--------------------------
    capture = cv2.VideoCapture(0)
    window_name = 'windows'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    #--------------------------
    # Execution
    #--------------------------
    while True:
        _, image = capture.read()  # get an image from the camera

    #--------------------------
    # Visualization
    #--------------------------
  
        cv2.imshow('window', image)  # Display the image
        cv2.waitKey(25)

    #--------------------------
    # Termination
    #-------------------------- 
    

if __name__ == '__main__':
    main()