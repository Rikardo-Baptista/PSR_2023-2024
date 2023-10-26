#!/usr/bin/env python3

#Exercicio 2a:
#Implemente um programa que faça a aquisição de uma imagem da câmara e 
#depois faça o seu display.

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