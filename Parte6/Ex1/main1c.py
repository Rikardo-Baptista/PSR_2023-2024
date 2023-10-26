#!/usr/bin/env python3 

#Exercicio 1c
#Crie um programa parecido com o paint. O programa deve ter um callback que recolhe a posição do rato
#e quando o botão esquerdo for pressionado o programa desenha pixeis de uma certa cor no ecrã. 
#O ecrã deve ser uma imagem de 600x400 inicializada toda branca.
#O programa deve ainda deve escutar as teclas:
    #tecla r, para mudar a cor a desenhar para vermelho
    #tecla g, para mudar a cor a desenhar para verde
    #tecla b, para mudar a cor a desenhar para azul

import argparse
from functools import partial
import cv2
import numpy as np
from colorama import Fore, Style

def mouseCallback(event, x, y, flags, *userdata, image_rgb, drawing_data):

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing_data['pencil_down'] = True
        print(Fore.BLUE + 'pencil_down set to True' + Style.RESET_ALL)
        
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing_data['pencil_down'] = False
        print(Fore.RED + 'pencil_down released' + Style.RESET_ALL)

    if drawing_data['pencil_down'] == True:
        # cv2.circle(image_rgb, (x, y), 3, (255,255,255), -1)
        cv2.line(image_rgb, (drawing_data['previous_x'], drawing_data['previous_y']), (x,y), drawing_data['color'], 1) 

    drawing_data['previous_x'] = x
    drawing_data['previous_y'] = y

def main():

    # -----------------------------------------------
    # Initialization 
    # -----------------------------------------------
    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--image_filename', type=str, help='', required=False, 
                        default='../images/atlascar.png')

    args = vars(parser.parse_args()) # creates a dictionary

    cv2.namedWindow("image_rgb")
    cv2.setMouseCallback("image_rgb", partial(mouseCallback, image_rgb=image_rgb, drawing_data=drawing_data))

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


##################################################################################

    #!/usr/bin/env python3 
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

    image_filename = args['image_filename']
    # image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image_rgb = np.ones((400,600,3), dtype=np.uint8) * 255
    # image_rgb = np.zeros((400,600), dtype=np.uint8) + 255

    h, w, nc = image_rgb.shape

    drawing_data = {'pencil_down': False, 'previous_x': 0, 'previous_y': 0, 'color': (255,255,255)}

    cv2.namedWindow("image_rgb")
    cv2.setMouseCallback("image_rgb", partial(mouseCallback, image_rgb=image_rgb, drawing_data=drawing_data))

    # -----------------------------------------------
    # Execution 
    # -----------------------------------------------

    # Draw circle on image
    xc = int(w/2)
    yc = int(h/2)
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
    while True:
        cv2.imshow('image_rgb', image_rgb)  # Display the image
        key = cv2.waitKey(50) # wait for a key press before proceeding

        if key == ord('q'): # quit program
            print('Quitting program')
            break
        elif key == ord('r'): # red color for pencil
            print('Setting pencil to red color')
            # TODO how to set the red color?
            drawing_data['color'] = (0,0,255)




    # -----------------------------------------------
    # Termination 
    # -----------------------------------------------
    cv2.destroyWindow('image_rgb')

if __name__ == '__main__':
    main()