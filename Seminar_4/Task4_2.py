"""Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.

НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
Расширить значение коэффициентов до [-100..100]"""


new_file1 = open('file1.txt', 'r')  # только для чтения
new_file2 = open('file2.txt', 'r')  # только для чтения
new_file3 = open('file3.txt', 'w')  # для перезаписи
file1 = new_file1.readline()
file2 = new_file2.readline()
for i in range(len(file1)):
    if file1[i-1] != '^':
        if file1[i].isnumeric():
            new_file3.write(str(int(file1[i]) + int(file2[i])))
        else:
            new_file3.write(str(file1[i]))
    else:
        new_file3.write(str(file1[i]))
new_file1.close()
new_file2.close()
new_file3.close()


