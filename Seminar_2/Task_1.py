"""Напишите программу, которая принимает на вход вещественное число
и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11"""

# num = input('Введите второе число: ')
# summa = 0
# for i in num:
#     if i == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0':
#         # не нашел я как их еще перечислить ))
#         summa= int(i)
# print(f"Сумма цифр числа {num} равна: ", summa

num = input('Введите число: ')
summa = 0
for i in num:
    if i.isdigit():  # возвращает True, если все символы в строке являются цифрами./
                     # 'Если нет, возвращается False
        summa += int(i)

print(f"Сумма цифр числа {num} равна: ", summa)

