# -*- coding: utf-8 -*-
# Archivo Base

import random

def run():
    
    number_found = False
    random_number = random.randint(0, 20)

    while not number_found:
        number = int(input('Type Number of 0 - 20: '))

        if number == random_number:
            print('congratulations you found the number')
            number_found = True
        elif number > random_number:
            print('the number is smaller')
        else:
            print('the number is bigger')

if __name__ == '__main__':
    run()