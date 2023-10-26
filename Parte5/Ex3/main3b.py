#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#Exercicio 3b:
#Apesar de funcional, o Exercício 3 a) tem o problema de necessitar de variáveis globais,
#que o são por terem de ser acedidas quer pela função main quer pela função onTrackbar.
#As variáveis globais não são recomendadas por terem vários problemas.
#Altere o Exercicio 3a de modo a não utilizar variáveis globais.
#Será necessário que a função receba como argumentos todas as variáveis de que necesita. Ver as funcionalidades da função partial.

import argparse
import cv2
from functools import partial

def onTrackbar(val, image_gray, window_name):
    _,image_thresholded = cv2.threshold(image_gray, val, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, image_thresholded)  # Show the image

def main():
    
    #Declaration variables
    window_name = 'window - Ex3b'
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
    cv2.createTrackbar('Threshold', window_name, 0, 255, 
                       partial(onTrackbar, image_gray=image_gray, window_name=window_name))
    #Setting position of threshold trackbar to 128
    cv2.setTrackbarPos('Threshold', window_name, val)
    
    onTrackbar(val, image_gray, window_name)
    
    cv2.waitKey(0)



if __name__ == '__main__':
    main()