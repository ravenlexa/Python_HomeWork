"""Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет"""

number = int(input('Введите номер дня недели и получите ответ - выходной или нет: '))
if number > 7 or number < 1:
    print('Нет такого номера дня недели')
else:
    if number < 6 and number > 0:
        print('Будни')
    if number < 8 and number > 5:
        print('Выходной')