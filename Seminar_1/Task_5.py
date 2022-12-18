
import math
print('Введите координаты первой точки: ')
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
print('Введите координаты второй точки: ')
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

result = math.sqrt(((x2-x1)**2+(y2-y1)**2))
print(result)

