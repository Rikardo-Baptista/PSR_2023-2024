#!/usr/bin/env python3

#Exercicio 3c:
#Finalmente, pretende-se que o programa seja capaz de perceber se
#a pessoa está a falar ou não.
#Esta classificação deve ser comunicada escrevendo texto na imagem mostrada.

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