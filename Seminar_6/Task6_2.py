"""Реализуйте алгоритм перемешивания списка.
НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
максимум использование библиотеки Random для и получения случайного int"""
from random import randint as RI

my_list = [RI(0, 100) for i in range(8)]
print(f'             Список: {my_list}')

def shafl_list():
    global my_list
    for i in range(len(my_list) - 1, 0, -1):
        j = RI(0, i + 1)
        my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list

my_list_list = shafl_list()
print(f'Перемешенный список: {my_list}')

'''Не знаю на сколько компактней стало))
Пытался то что в функции тоже в одну строку сделать, костыли получаются.
Поэтому оставил так.'''