# -*- coding: utf8 -*-

# Calculadora convertidor de soles a dolares 

CHANGE_COIN = 3.3

def foreign_exchange_calculator(ammount):
    return CHANGE_COIN * ammount

def run():
    print('Calculadora de Divisas')
    print('Convierte Soles a Dolares')
    print('')

    ammount = float(input('Ingresa la cantidad de soles que desea convertir: '))

    result = foreign_exchange_calculator(ammount)
    print('S/. {} soles son $ {} dolares '.format(ammount, result))
    print('')

if __name__ == '__main__':
    run() 