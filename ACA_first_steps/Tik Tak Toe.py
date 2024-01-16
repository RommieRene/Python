board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],
]

import random

def print_board():
    for row in board:
        for item in row:
            print(item, end=' ')
        print()
        # print(' '.join(row))


def user_move():
    while True:
        try:
            # get user input x,y ==> '1,3'
            coordinates = input('X,Y: ').split(',')
            if len(coordinates) != 2:
                raise ValueError('Invalid length')

            x, y = coordinates
            if not x.isdigit() or not y.isdigit():
                raise ValueError('Non numeric value')

            x = int(x)
            y = int(y)

            # validate x, y in (1, 3)
            if x not in range(1, 4) or y not in range(1, 4):
                raise ValueError('Must be number in range 1:3')

            if board[x - 1][y - 1] != '_':  # is position available (== '_')
                raise ValueError('Position is not available')

            board[x - 1][y - 1] = 'X'
            break
        except ValueError as ex:
            print(ex)


def pc_move():
#     # ranomly select an available position
#     # and change it to 'O'
     while True:
        try:
            # get user input x,y ==> '1,3'

            x = random.randrange(1, 4)
            y = random.randrange(1, 4)

            # validate x, y in (1, 3)


            if board[x - 1][y - 1] != '_':  # is position available (== '_')
                raise ValueError('Position is not available')

            board[x - 1][y - 1] = 'O'
            break
        except ValueError as ex:
            print(ex)

def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != '_':
            return row[0]
        elif board[0][2] == board[1][2] == board[2][2] != '_':
            return board[0][2]
        elif board[0][0] == board[1][0] == board[2][0] != '_':
            return board[0][0]
        elif board[0][1] == board[1][1] == board[2][1] != '_':
            return board[0][1]
        elif board[0][0] == board[1][1] == board[2][2] != '_':
            return board[0][0]
        elif board[0][2] == board[1][1] == board[2][0] != '_':
            return board[0][2]




winner = None
while not winner:
    print_board()
    user_move()
    winner = check_winner()

    print_board()
    print('-----------')
    pc_move()
    winner = check_winner()
print('Winner',winner)
