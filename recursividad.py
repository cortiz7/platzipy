# -*- coding: utf-8 -*-

# Recursividad : Encontral el factorial de un Nro

def factorial(number):
    if number == 0:
        return 1
    
    return number * factorial(number - 1)
    

def run():
    number = int(input('Input Number: '))
    result = factorial(number)
    
    print('The factorial of {} is: {}'.format(number, result))
    

if __name__ == '__main__':
    run()