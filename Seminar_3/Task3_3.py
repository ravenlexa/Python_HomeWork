"""Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19"""
import random

num = int(input('Введите размер списка '))
my_list = []
for i in range(num):
    float = random.uniform(0, 9)
    my_list.append(round(float, random.randint(0, 3)))

print(my_list)

new_list = []

for i in my_list:
    if i != int(i):
        new_list.append(round(i % 1, 3))
print(new_list)
print(f'Разница между масимальной ({max(new_list)}) и минимальной ({min(new_list)})'
      f'дробными частями будет ({max(new_list)-min(new_list)})')

