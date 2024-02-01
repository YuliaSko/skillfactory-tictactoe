board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}


def print_board(board):
    print(board['1'] + ' |' + board['2'] + ' |' + board['3'])
    print('--+--+--')
    print(board['4'] + ' |' + board['5'] + ' |' + board['6'])
    print('--+--+--')
    print(board['7'] + ' |' + board['8'] + ' |' + board['9'])


def get_move():
    move = input('Введи номер ячейки: ')
    return move


def check_win(board):
    if board['1'] == board['2'] == board['3'] != ' ':
        return True
    elif board['4'] == board['5'] == board['6'] != ' ':
        return True
    elif board['7'] == board['8'] == board['9'] != ' ':
        return True
    elif board['1'] == board['4'] == board['7'] != ' ':
        return True
    elif board['2'] == board['5'] == board['8'] != ' ':
        return True
    elif board['3'] == board['6'] == board['9'] != ' ':
        return True
    elif board['1'] == board['5'] == board['9'] != ' ':
        return True
    elif board['3'] == board['5'] == board['7'] != ' ':
        return True
    else:
        return False


def game():

    turn = 'X'
    count = 0

    for i in range(10):
        print_board(board)
        print('Твой ход', turn)
        print('(левая верхняя ячейка - 1, правая нижняя -9)')

        move = get_move()

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print('Ячейка занята, выбери другу ячейку')
            continue

        if count >= 5:
            if check_win(board):
                print_board(board)
                print('Игра окончена')
                print('***', turn, 'win ***')
                break
            elif count == 9:
                print_board(board)
                print('Игра окончена')
                print('*** Ничья ***')
                break

        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'


game()

