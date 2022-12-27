"""Задана натуральная степень k.
Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.
Пример:
если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 """
import itertools
from random import randint

print('Чтобы сформировать многочлен степени k и записать в файл, введите степень k! ')
k = int(input("Введите степень k: "))

index = []
for i in range(1, k + 2):
    index.append(randint(1, 101))
    #print(index)

result = []
for i in range(len(index)):
    if k == 1:
        result.append(f'{index[i]}*x')
    elif k == 0:
        result.append(f'{index[i]}')
    else:
        result.append(f'{index[i]}*x^{k}')
    signs = randint(0, 1) # вставляем рандомные знаки
    if signs == 1:
        result.append('+')
    elif signs == 0:
        result.append('-')
    k -= 1

result.pop(-1)  # убираем последний знак (+ или -)
result.append('=0')  # добавляем в конце к любому многочлену
print(''.join(result))



