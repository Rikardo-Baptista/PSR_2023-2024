#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

import argparse
import cv2
import numpy as np


#Exercício 2d: 
#Usando a função cv2.inRange crie uma máscara dos pixeis com valores de rgb entre (bmin, gmin, rmin) e (bmax, gmax, rmax). 
#Parametrize de modod a segmentar o caixote verde por trás dos robôs.

def main():

    #--------------------------
    # Processing
    #--------------------------

    image_filename = '../images/atlas2000_e_atlasmv.png'
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    #--------------------------
    # Execution
    #--------------------------
    
    #Mask to detection green
    lower_bound = np.array([0, 60, 0])
    upper_bound = np.array([50, 255, 50])
    image_mask = cv2.inRange(image_rgb, lower_bound, upper_bound)
   
    # ----------------------
    # Visualization
    # ----------------------

    cv2.imshow('RGB_Image', image_rgb)  # Display the image
    cv2.imshow("Mask_Image", image_mask) # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

    # ----------------------
    # Termination
    # ----------------------


if __name__ == '__main__':
    main()