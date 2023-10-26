#!/usr/bin/env python3 

import argparse
import cv2
import time

def main():

    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--image_filename', type=str, help='', required=False, 
                        default='../images/atlascar.png')
    args = vars(parser.parse_args()) # creates a dictionary

### Código em modo arcaico

  #  while True:
  #      image = cv2.imread('../images/atlascar.png', cv2.IMREAD_COLOR) # Load an image
  #      cv2.imshow('window', image)  # Display the image
  #      cv2.waitKey(3000) # wait for a key press before proceeding

  #       image = cv2.imread('../images/atlascar2.png', cv2.IMREAD_COLOR) # Load an image
  #       cv2.imshow('window', image)  # Display the image
  #       cv2.waitKey(3000) # wait for a key press before proceeding


### Código utilizando flip-flop (variar alternadamente uma variavel, isto é, está a 0 passa a 1, está a 1 passa a 0, etc......)
    image_1 = cv2.imread('../images/atlascar.png', cv2.IMREAD_COLOR) # Load an image_1
    image_2 = cv2.imread('../images/atlascar2.png', cv2.IMREAD_COLOR) # Load an image_2
    
    flip_flop = True

    while True:
        #if flip_flop:
        #    flip_flop = False
        #else:
        #    flip_flop = True

        flip_flop = not flip_flop #Substituindo o if..else anterior

        if flip_flop:
            cv2.imshow('window', image_1)  # Display the image
        else:
            cv2.imshow('window', image_2)  # Display the image
    
        cv2.waitKey(3000) # wait for a key press before proceeding

if __name__ == '__main__':
    main()