"""Создайте программу для игры в 'Крестики-нолики'
НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом"""

field = list(range(1, 10))
winning_combinations = [[0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8],
                        [0, 3, 6],
                        [1, 4, 7],
                        [2, 5, 8],
                        [0, 4, 8],
                        [2, 4, 6]]


def print_field(field):
    print('_____________')
    for i in range(3):
        print('|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3], '|')
        print('_____________')


def draw_field(step, symbol):
    ind = field.index(step)
    field[ind] = symbol


def get_result():
    winner = ''

    for i in winning_combinations:
        if field[i[0]] == 'X' and field[i[1]] == 'X' and field[i[2]] == 'X':
            winner = 'X'
        if field[i[0]] == 'O' and field[i[1]] == "O" and field[i[2]] == 'O':
            winner = 'O'

    return winner


game_over = False
player1 = True

while not game_over:
    print_field(field)

    if player1:
        symbol = 'X'
        step = int(input('Игрок 1, ваш ход: '))
    else:
        symbol = 'O'
        step = int(input('Игрок 2, ваш ход: '))

    draw_field(step, symbol)
    winner = get_result()
    if winner != '':
        game_over = True
    else:
        game_over = False

    player1 = not player1

print_field(field)
print('Победили', winner)
