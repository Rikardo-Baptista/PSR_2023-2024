#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here
from colorama import Fore, Back, Style
from time import time
import math
from collections import namedtuple

#Exercício 3 - Números Complexos (Utilizar Named Tuples)
# Sugere-se a utilização de namedTuples que são tuplos 
# que permitem nomear cada um dos items para posterior utilização

def addComplex(x, y):
    realPart = x.real + y.real
    imaginaryPart = x.imag + y.imag
    complexTuple = Complex(realPart, imaginaryPart)
    return complexTuple

def multiplyComplex(x, y):
    realPart = x.real*y.real - x.imag*y.imag
    imaginaryPart = x.real*y.imag + x.imag*y.real
    complexTuple = Complex(realPart, imaginaryPart)
    return complexTuple

def printComplex(x):
    realPart = x.real
    imaginaryPart = x.imag
    print(str(realPart) + ' ' + str(imaginaryPart)+'i' )

Complex = namedtuple('Complex', ['real', 'imag'])

def main():
    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)
    c2 = Complex(-2, 7)
    print('c1 = ' + str(c1)) # named tuple looks nice when printed

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))


if __name__ == '__main__':
    main()