"""Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]"""
import random

num = int(input('Введите размер списка '))
my_list = []
my_list2 = []

for i in range(num):
    my_list.append(random.randint(1, 9))

for i in range(len(my_list)):
    while i < len(my_list)/2 and num > len(my_list)/2:
        num = num - 1
        x = my_list[i] * my_list[num]
        my_list2.append(x)
        i += 1

print(my_list)
print(my_list2)

