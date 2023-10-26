#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#Exercicio 3d:
#Implemente um programa que permita configurar a segmentação de cor. 
#O programa deve executar a segmentação verificando quais os pixeis 
#da imagem que estão dentro de certos limites mínimo e máximo. 
#Estes limites deverão ser diferentes para cada canal de cor. 

import argparse
import json
import cv2
from functools import partial

def onTrackbar(val, image_gray, window_name):
    _,image_thresholded = cv2.threshold(image_gray, val, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, image_thresholded)  # Show the image

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('({}, {})'.format(x,y))


def main():
    
    #Declaration variables
    window_name = 'window - Ex3c'
    image_gray = None
    val = 128

    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--image_filename', type=str, help='', required=False, 
                        default='../images/atlascar.png')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image_filename'], cv2.IMREAD_COLOR) # Load an image
    cv2.imshow('Original', image) #Visualizar imagem original
    
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    
    cv2.namedWindow(window_name)
    #cv2.createTrackbar
    cv2.createTrackbar('', window_name, 0, 255, 
                       partial(onTrackbar, image_gray=image_gray, window_name=window_name))
    #Setting position of threshold trackbar to 128
    cv2.setTrackbarPos('Threshold', window_name, val)
    cv2.setMouseCallback(window_name, onMouse)
    
    onTrackbar(val, image_gray, window_name)
    
    cv2.waitKey(0)

    file_name = 'limits.json'
    with open(file_name, 'w') as file_handle:
        print('writing dictionary d to file ' + file_name)
        json.dump(d, file_handle) # d is the dicionary

    # FaLtA alterar CODIGO


if __name__ == '__main__':
    main()