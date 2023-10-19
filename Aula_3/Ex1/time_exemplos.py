#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here
from colorama import Fore, Back, Style
from time import time

# define functions here ...
def main():
# import the time module
    import time

# get the current time in seconds since the epoch
    seconds = time.time()

    print("Seconds since epoch =", seconds)	

# convert the time in seconds since the epoch to a readable format
    local_time = time.ctime(seconds)

    print("Local time:", local_time)

# Atrasar o tempo de impressão
    print("Printed immediately.")
    time.sleep(2.4)
    print("Printed after 2.4 seconds.")

# Converte o tempo (segundos) em formato data (Ano,mes,hora)
    result = time.localtime(seconds)
    print("result:", result)
    print("\nyear:", result.tm_year)
    print("tm_hour:", result.tm_hour)

# Converte o tempo (segundos) em formato data (Ano,mes,hora) em UTC (menos 1 hora)
    result = time.gmtime(seconds)
    print("result:", result)
    print("\nyear:", result.tm_year)
    print("tm_hour:", result.tm_hour)

if __name__ == "__main__":
    main()