# -*- coding: utf-8 -*-

# calcular si un numero es primo

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            print(number)
            if number % i == 0:
                return False
    return True

def run():
    number = int(input('Escribe un numero: '))
    result = is_prime(number)

    if result:
        print('Tu nro es Primo')
    else:
        print('Tu nro No es Primo')


if __name__ == '__main__':
    run()