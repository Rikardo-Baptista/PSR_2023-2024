#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

import argparse
import cv2

def main():

    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--image_filename', type=str, help='', required=False, 
                        default='../images/atlascar.png')

    args = vars(parser.parse_args()) # creates a dictionary
    print(args)

    image_filename = args['image_filename']
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY) 

    retval, image_thresholded = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)
    #Imagem thresholded tem o valor de decisão em 128 (a meio da escala)
    #Se valor de decisão for próximo de 0 temos cores brancas
    #Se valor de decisão for proximo de 255 temos cores pretas

    cv2.imshow('image_rgb', image_rgb)  # Display the image
    cv2.imshow('image_gray', image_gray)  # Display the image
    cv2.imshow('image_thresholded', image_thresholded)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()