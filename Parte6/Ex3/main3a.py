#!/usr/bin/env python3

#Exercicio 3a:
#Pretende-se desenvolver uma aplicação em python opencv que seja capaz 
#de detetar caras num stream de video.
#A face detetada deve ser destacada na imagem mostrada, ficando mais esverdeada.

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