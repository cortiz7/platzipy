# -*- coding: utf-8 -*-

# Separacion de cadena de texto

def run():
    my_styring = 'platzi'

    #return character of string
    print(my_styring[1])

    #return strings start - end 
    print(my_styring[1:])

    #return strings cahracter start - character end (not included last character)
    print(my_styring[1:3])

    #return strings start - end , jump 2 
    print(my_styring[1:6:2])

    #return strings end - start, jump -1 
    print(my_styring[::-1])


if __name__ == '__main__':
    run()