#!/usr/bin/env python3 

import argparse
import cv2

def main():

    #--------------------------
    # Initialization
    #--------------------------

    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--image_filename', type=str, help='', required=False, 
                        default='../images/atlascar.png')

    args = vars(parser.parse_args()) # creates a dictionary
    print(args)

    image_filename = args['image_filename']
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY) 

    # Window name in which image is displayed 
    #window_name = 'Image'
   
   

    #--------------------------
    # Execution
    #--------------------------

    image_filename = '../images/atlascar.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    #cv2.circle(image, center_coordinates, radius, color, thickness)
    
    h, w, nc = image_rgb.shape

    xc = (w//2)
    xd = (h//2)

     # Center coordinates 
    center_coordinates = (xc, xd) 
    # Radius of circle 
    radius = 20
    # Blue color in BGR 
    color = (255, 0, 0) 
    # Line thickness of 2 px 
    thickness = 2 # se for valor -1 preenche a azul o circulo


    cv2.circle(image_rgb, center_coordinates, radius, color, thickness)

    #--------------------------
    # Visualization
    #--------------------------

    #cv2.imshow('window', image)  # Display the image
    cv2.imshow('window', image_rgb)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

    #--------------------------
    # Termination
    #--------------------------

if __name__ == '__main__':
    main()


    # Falta codigo !!!!