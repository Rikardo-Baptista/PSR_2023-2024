#!/usr/bin/env python3

#Exercicio 2b:
#Adapte o exercício anterior de modo a implementar um programa que faça a aquisição 
#e display contínuos da imagem da câmara do seu portátil.

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
    while True:
        _, image = capture.read()  # get an image from the camera

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