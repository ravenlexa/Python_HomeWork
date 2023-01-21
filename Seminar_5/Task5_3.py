with open('My_text.txt', 'w', encoding='utf_8') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))
with open('My_text.txt', 'r', encoding='utf_8') as file:
    my_text = file.readline()
    txt_compr = my_text.split()


def file_encod(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


txt_compr = file_encod(my_text)

with open('cipher_text.txt', 'w', encoding='utf_8') as file:
    file.write(f'{txt_compr}')
print(txt_compr)

input('Для восстановления текста нажмите Enter')

with open('cipher_text.txt.', 'r', encoding='utf_8') as file:
    text = file.read()

number = ''
text_return = ''
for i in text:
    if i.isdigit():
        number = number + i
    else:
        text_return += int(number)*i
        number = ''

print(f'Восстановленный текст представляет последовательность:\n{text_return}')

with open('My_text.txt.', 'w', encoding='utf_8') as file:
    file.write(text_return)
