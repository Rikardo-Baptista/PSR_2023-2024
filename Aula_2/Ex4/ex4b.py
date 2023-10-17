#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

import argparse

# Use imports here
from colorama import Fore, Back, Style
from my_functions import isPerfect


def main():
    # Process command line arguments
    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-mn', '--maximum_number', type=int, help='max number.', required=True)
    parser.add_argument('-n', '--name', type=str, help='A name to print.', required=False, default='Antonio')
    parser.add_argument('-sl', '--say_hello', help='Say hello?', action='store_true')

    args = vars(parser.parse_args()) # creates a dictionary
    print(args)

    if args['say_hello']:
        print("Hi " + args['name'] + " !!!")

    print("Starting to compute perfect numbers up to " + str(args['maximum_number']))
    for i in range(1, args['maximum_number']+1):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')

if __name__ == "__main__":
    main()
