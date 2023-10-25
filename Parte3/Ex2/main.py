#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here
from colorama import Fore, Back, Style
from time import time
import math

#Exercício 2 - Números Complexos
# O objetivo é implementar código python que faça 
# a gestão de operações com números complexos (Soma, Multiplicação e Resultado)

# define functions here ...
def addComplex(x, y):
    realPart = x[0] + y[0]
    imaginaryPart = x[1] + y[1]
    complexTuple = (realPart, imaginaryPart)
    return complexTuple

def multiplyComplex(x, y):
    realPart = x[0]*y[0] - x[1]*y[1]
    imaginaryPart = x[0]*y[1] + x[1]*y[0]
    complexTuple = (realPart, imaginaryPart)
    return complexTuple

def printComplex(x):
    realPart = x[0]
    imaginaryPart = x[1]
    print(str(realPart) + ' ' + str(imaginaryPart)+'i' )

def main():
   # Define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # Test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()