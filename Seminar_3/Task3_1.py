import random

my_list = []
summa = 0
for i in range(8):
    my_list.append(random.randint(0, 100))
print(f'Список: {my_list}')
for i in range(len(my_list)):
    if i % 2 != 0:
        summa += my_list[i]

print(f'Сумма нечетных чисел равна: {summa}')
