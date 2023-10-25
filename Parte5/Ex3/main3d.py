#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

import argparse
import cv2
import numpy as np


def main():

    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--image_filename', type=str, help='', required=False, 
                        default='../images/atlas2000_e_atlasmv.png')

    args = vars(parser.parse_args()) # creates a dictionary
    print(args)

    image_filename = args['image_filename']
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    

    lower_bound = np.array([35, 100, 100])
    upper_bound = np.array([85, 255, 255])

    mask = cv2.inRange(image_rgb, lower_bound, upper_bound)

    #Aplicar a máscara na imagem original para destacar a cor verde
    image_mask = cv2.bitwise_and(image_rgb, image_rgb, mask=mask)



    cv2.imshow('image_rgb', image_rgb)  # Display the image
    cv2.imshow("image_mask.png", image_mask)
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()