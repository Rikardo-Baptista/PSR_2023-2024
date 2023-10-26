#!/usr/bin/env python3

#Exercicio 3b
#Nas regiões da imagem que não estão incluídas pela cara detetada, 
#pretende-se detetar arestas e destacá-las avermelhando-as na imagem mostrada.

import argparse
import cv2

def main():

    #--------------------------
    # Initialization
    #--------------------------
    capture = cv2.VideoCapture(0)
    window_name = 'window'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    #--------------------------
    # Execution
    #--------------------------

    #--------------------------
    # Visualization
    #--------------------------
    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(25)

    #--------------------------
    # Termination
    #-------------------------- 


if __name__ == '__main__':
    main()