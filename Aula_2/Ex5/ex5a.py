#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

# Use imports here
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

#Ex5a
    # Usando como ponto de partida o exercício 4, alterar a função anterior para criar uma lista dos inputs realizados 
    # e processar essa lista (para calcular o número de digitos/outros) a posteriori.
    n_numeric = 0
    n_others = 0
    for key in keys:
        if key.isnumeric():
            n_numeric +=1
        else:
            n_others +=1

    print('You pressed on ' + str(n_numeric) + ' numeric keys')
    print('You pressed on ' + str(n_others) + ' others keys')

def main():
    countNumbersUpto('x')

if __name__ == "__main__":
    main()