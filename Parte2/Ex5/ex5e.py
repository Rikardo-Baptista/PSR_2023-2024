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
    print('Ex5a')
    print('You pressed on ' + str(n_numeric) + ' numeric keys')
    print('You pressed on ' + str(n_others) + ' others keys\n')

#Ex5b
    # Crie uma lista que contenha apenas os inputs numéricos que foram inseridos (pela ordem em que foram inseridos).
    numerical_keys = []
    others_keys = []

    for key in keys:
        if key.isnumeric():
            numerical_keys.append(key)
        else:
            others_keys.append(key)
    print('Ex5b')
    print('Numerical_keys' + str(numerical_keys))
    print('Others_keys' + str(others_keys) + '\n')
    
#Ex5c
    # Crie um dicionário apenas com os inputs other em que as chaves são a ordem dos inputs inseridos e o valor são os inputs.
    
    #Solução 1:
    #Utilizando uma variavel i como contador (solução arcaica)
    #d_keys = {}
    #i = 0
    #for key in keys:
    #    d_keys[i] = key
    #    i = i + 1

    #Solução 2:
    #Utilizando a função do python enumerate
    d_keys = {}
    for key_idx, key in enumerate(keys):
        d_keys[key_idx] = key

    print('Ex5c')
    print('d_keys = ' + str(d_keys) + '\n')

#Ex5d
    # Reordene a lista da alínea 5 b) de modo a que esteja por ordem crescente do valor dos inputs.
    numerical_keys.sort()
    print('Ex5d')
    print('Numerical_keys_order = ' + str(numerical_keys) + '\n')

#Ex5e
    #Refazer a alínea 5 b) usando uma list comprehension.
    numerical_keys2 = [ x for x in keys if x.isnumeric()]
    print('Ex5e')
    print('Numerical_keys2_order = ' + str(numerical_keys2))

    d_keys2 = {idx:x for idx, x in enumerate(keys)}
    print('d_keys2 = ' + str(d_keys2))

def main():
    countNumbersUpto('x')

if __name__ == "__main__":
    main()