#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

import argparse
import cv2

#Exercício 2b:
#

def main():

    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--image_filename', type=str, help='', required=False, 
                        default='../images/atlascar.png')

    args = vars(parser.parse_args()) # creates a dictionary
    print(args, '\n')

    image_filename = args['image_filename']
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    #Imagem thresholded tem o valor de decisão em 128 (a meio da escala)
    #Se valor de decisão for próximo de 0 temos cores brancas
    #Se valor de decisão for proximo de 255 temos cores pretas
    retval, image_thresholded = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)
  
    print('Image_rgb type:', type(image_rgb))
    print('Image_rgb dtype:', image_rgb.dtype)
    print('Image_rgb shape:', image_rgb.shape, '\n')
    print('Image_gray type:', type(image_gray))
    print('Image_gray dtype:', image_gray.dtype)
    print('Image_gray shape:', image_gray.shape, '\n')
    print('Image_thresholded type:', type(image_thresholded))
    print('Image_thresholded dtype:', image_thresholded.dtype)
    print('Image_thresholded shape:', image_thresholded.shape, '\n')
   
    cv2.imshow('image_rgb', image_rgb)  # Display the image
    cv2.imshow('image_gray', image_gray)  # Display the image
    cv2.imshow('image_thresholded', image_thresholded)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

if __name__ == '__main__':
    main()