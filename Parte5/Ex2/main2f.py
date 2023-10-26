#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

import argparse
import cv2
import numpy as np
from copy import deepcopy

#Exercício 2f: 
#Usando uma adição da imagem original por um escalar para cada canal,
#pinte de vermelho o caixote verde detetado na alínea anterior.

def main():

    #--------------------------
    # Processing
    #--------------------------

    image_filename = '../images/atlas2000_e_atlasmv.png'
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    #--------------------------
    # Execution
    #--------------------------
    
    #Green color detection
    lower_bound = np.array([0, 60, 0])
    upper_bound = np.array([50, 255, 50])
    image_mask = cv2.inRange(image_rgb, lower_bound, upper_bound)

    #Paint red areas detected as green
    
    #Split Channels
    image_b, image_g, image_r = cv2.split(image_rgb) 

    #Tratar a imagem com os canais separados
    # Importante: Necessitamos de converter a image_mask para booleana
    # Fazendo image_mask.astype(bool)
    image_b[image_mask.astype(bool)] = 0 
    image_g[image_mask.astype(bool)] = 0
    image_r[image_mask.astype(bool)] = 255
    
    #Merge Channels
    image_rgb = cv2.merge([image_b, image_g, image_r]) 

    # ----------------------
    # Visualization
    # ----------------------

    cv2.imshow('RGB_Image', image_rgb)  # Display the image
    cv2.imshow("R_Channel", image_r) # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

    # ----------------------
    # Termination
    # ----------------------

if __name__ == '__main__':
    main()