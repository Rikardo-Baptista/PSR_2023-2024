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
    
    #capture = cv2.VideoCapture(./areyouspeaking.mp4')
    capture = cv2.VideoCapture(0)
    window_name = 'window'
    cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
    #cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    face_classifier = cv2.CascadeClassifier(cv2.data.harcasca)
   
    #--------------------------
    # Execution
    #--------------------------
    while True:
        _, image_rgb = capture.read()  # get an image from the camera
        image_gray=cv2.cvtColor(image_rgb,)
    #--------------------------
    # Visualization
    #--------------------------
        #cv2.imshow('window', image)  # Display the image
        cv2.waitKey(25)

    #--------------------------
    # Termination
    #-------------------------- 

if __name__ == '__main__':
    main()