#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

# Use imports here
import argparse
import readchar
from colorama import Fore, Back, Style

def ReadAllCharsUpTo(stop_char):
    chars = []
    while True:
        chars.append(readchar.readchar())
        print(chars[-1])
        if chars[-1] == stop_char:
            break


def main():

    ReadAllCharsUpTo('x')

if __name__ == "__main__":
    main()


###Alterar codigo