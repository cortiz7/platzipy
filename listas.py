# -*- coding: utf-8 -*-
# Listas
def average_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += float(temp)
    return sum_of_temps/len(temps)


def run():
    #friends = []
    #friends = list()
    temperatures = [21, 24, 24, 22, 20, 23, 24]
    average = average_temps(temperatures)
    print('The tempearature average is: {0:.2f}'.format(average))

    my_list_1 = []
    my_list_1.append(1)
    my_list_2 = [2, 8, 4]
    my_list_3 = my_list_1 + my_list_2
    my_list_3.sort()
    print(my_list_3)

    my_list_4 = ['a']
    my_list_5 = my_list_4 * 2
    print(my_list_5)

    my_list_name = ['juan', 'pedro', 'pepe']
    my_list_name[1] = 'rodrigo'
    print(my_list_name)
    my_list_name.extend(my_list_5)
    print(my_list_name)    
    my_list_name.sort()
    del my_list_name[3]
    print(my_list_name)

    string_house = 'house'
    list_house = list(string_house)
    print (list_house)
    str_house_1 = ''.join(list_house)
    print(str_house_1)

    
if __name__ == '__main__':
    run()