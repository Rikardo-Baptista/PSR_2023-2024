#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here
from colorama import Fore, Back, Style
from time import time
import math

# define functions here ...

def main():
    inicio = time()
    value = 50000000
    
    for i in range(1,value):
        resultado = math.sqrt(i)
        #print("Resultado:", resultado)

    fim = time()
    print('A funcao demorou: ' + str(round(fim - inicio , 2)) + ' segundos ' 
          + 'a ser executada!') 

if __name__ == "__main__":
    main()