#!/usr/bin/env python3 

#Exercicio 1a:
#Carregue a imagem atlascar.png e desenhe um círculo no seu centro com a função cv2.circle.

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
    #Desenhar um circulo ao centro da imagem_rgb com raio 55 e cor azul(255,0,0) com espessura do traço de 1.
    cv2.circle(image_rgb, (xc, yc), 55, (255,0,0), 1)
    #Desenhar um circulo ao centro da imagem_rgb com raio 55 e cor azul(255,0,0) com enchimento total.
    #cv2.circle(image_rgb, (xc, yc), 55, (255,0,0), -1)

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