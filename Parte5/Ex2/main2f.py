#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

import argparse
import cv2
import numpy as np
from copy import deepcopy


def main():

    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--image_filename', type=str, help='', required=False, 
                        default='../images/atlas2000_e_atlasmv.png')

    args = vars(parser.parse_args()) # creates a dictionary
    print(args)

    image_filename = args['image_filename']
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([40, 100, 50])
    upper_bound = np.array([70, 255, 255])

    mask = cv2.inRange(image_hsv, lower_bound, upper_bound)
    #print(mask.dtype)
    #print(mask.shape)

    #Aplicar a máscara na imagem original para destacar a cor verde
    image_mask = cv2.bitwise_and(image_hsv, image_hsv, mask=mask)
    image_rgb2 = deepcopy(image_rgb)

    #Separar a imagem em RGB
    image_b, image_g, image_r = cv2.split(image_rgb2) 

    #Tratar a imagem com os canais separados
    image_b[mask.astype(bool)] = 0
    image_g[mask.astype(bool)] = 255
    image_r[mask.astype(bool)] = 0
    
    #Juntar a imagem em RGB (nova)
    image_rgb2 = cv2.merge([image_b, image_g, image_r]) 


    #cv2.imshow('image_rgb', image_rgb)  # Display the image
    cv2.imshow("image_mask", mask)
    #cv2.imshow("image_rgb2", image_rgb2)
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()