"""Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19"""
import random

num = int(input('Введите размер списка '))
my_list = []
for i in range(num):
    f = random.uniform(0, 9)
    my_list.append(round(f, 2))

minn = my_list[0]
maxx = 0
for i in range(len(my_list)):

    if maxx < my_list[i]:
        maxx = my_list[i]
    if minn > my_list[i]:
        minn = my_list[i]
dif = (maxx - int(maxx)) - (minn - int(minn))

print(my_list)
print(maxx, minn)
print(round(dif, 2))
