#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

# Use imports here
from colorama import Fore, Back, Style
import readchar

# Define functions here ...
def  countNumbersUpto(stop_char):

    print('Start typing')

    keys =[]
    while True:
        key = readchar.readkey()
        keys.append(key)
        print('You typed ' + key)

        if key == stop_char:
            break

    print('\n' + str(keys) + '\n')

    n_numeric = 0
    for key in keys:
        if key.isnumeric():
            n_numeric +=1   
    print('You pressed on ' + str(n_numeric) + ' numeric keys' + '\n')

#Exemplo utilização do colorama da Aula_2 no Ex5 
    for idx_key, key in enumerate(keys):
        print(Fore.RED + str(idx_key) + Style.RESET_ALL + ': the key pressed was ' + Fore.GREEN + 
              Back.MAGENTA + key + Style.RESET_ALL) 

def main():
    countNumbersUpto('x')


if __name__ == "__main__":
    main()