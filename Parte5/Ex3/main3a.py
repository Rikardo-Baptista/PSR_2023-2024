#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#Exercicio 3a:
#Partindo do exercício 2 a) implemente uma trackbar que permita ao utilizador
#definir o limite de binarização a ser utilizado na binarização.

import argparse
import cv2

# Global variables
window_name = 'window - Ex3a'
image_gray = None
val = 128

def onTrackbar(val):
    _,image_thresholded = cv2.threshold(image_gray, val, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, image_thresholded)  # Show the image

def main():
    
    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--image_filename', type=str, help='', required=False, 
                        default='../images/atlascar.png')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image_filename'], cv2.IMREAD_COLOR) # Load an image
    cv2.imshow('Original', image) #Visualizar imagem original
    
    global image_gray # use global var
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    
    cv2.namedWindow(window_name)
    #cv2.createTrackbar
    cv2.createTrackbar('Threshold', window_name, 0, 255, onTrackbar)
    #Setting position of threshold trackbar to 128
    cv2.setTrackbarPos('Threshold', window_name, val)
    onTrackbar(val)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
