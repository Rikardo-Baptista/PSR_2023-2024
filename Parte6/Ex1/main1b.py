#!/usr/bin/env python3 

#Exercicio 1b:
#Adicione o texto 'PSR' à imagem a vermelho usando a funçao cv2.putText()

import argparse
from functools import partial
import cv2
import numpy as np
from colorama import Fore, Style

def main():

    # -----------------------------------------------
    # Initialization 
    # -----------------------------------------------
    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--image_filename', type=str, help='', required=False, 
                        default='../images/atlascar.png')

    args = vars(parser.parse_args()) # creates a dictionary

    # -----------------------------------------------
    # Execution 
    # -----------------------------------------------

    image_rgb = cv2.imread(args['image_filename'], cv2.IMREAD_COLOR)
    h, w, nc = image_rgb.shape

    # Draw circle on image
    xc = int(w/2) # w//2 - divisão inteira do numero
    yc = int(h/2) # h//2 - divisão inteira do numero
    #Desenhar um circulo ao centro da imagem_rgb com raio 55 e cor azul(255,0,0) com enchimento total.
    cv2.circle(image_rgb, (xc, yc), 55, (255,0,0), -1)
    
    # Add text to image
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (50, 100) 
    fontScale = 3
    color = (0, 0, 255) 
    thickness = 2
    image_rgb = cv2.putText(image_rgb, 'PSR', org, font, fontScale, color, thickness, cv2.LINE_AA) 

    # -----------------------------------------------
    # Visualization 
    # -----------------------------------------------
    cv2.imshow('image_rgb', image_rgb)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

    # -----------------------------------------------
    # Termination 
    # -----------------------------------------------
    cv2.destroyWindow('image_rgb')

if __name__ == '__main__':
    main()