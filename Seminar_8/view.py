import model


def input_class():
    return input('С каким классом работаем?'
                 '\n==> ').upper()


def not_class():
    print('Такого класса нет!')


def list_of_subject(subject_list: list):
    for i, subject in enumerate(subject_list, 1):
        print(f'{i}. {subject:5}')


def input_subject():
    return input('Какой предмет?'
                 '\n==> ').lower()


def not_subject():
    print('Такого предмета нет!')


def who_answer():
    return input('Кто будет отвечать?'
                 '\n==> ')


def not_student():
    print('Такого ученика нет!')


def what_mark():
    return input('На какую оценку ответил?'
                 '\n==> ')


def not_mark():
    print('Такой оценки не существует в нашей стране!!!')


def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')
