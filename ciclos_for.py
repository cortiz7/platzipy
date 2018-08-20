# -*- coding: utf-8 -*-
# Ciclos for 

def run():
    #Use continue
    for i in range(30):
        if i % 3 != 0:
            continue
        else:
            print(i)
    print('*********')

    #Use break
    for i in range(30):
        if i % 3 == 0:
            print(i)
        elif i == 22:
            break    
    print('*********ñ')

    #Use iterator string
    my_string = 'platzi'
    for i in my_string:
        print(i)

if __name__ == '__main__':
    run()