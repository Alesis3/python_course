import os

import readchar

board = [' | | | | | | ',
         ' | | | | | | ',
         ' | | | | | | ',
         ' | | | | | | ',
         ' | | | | | | ',
         ' | | | | | | ']

HEIGHT = len(board)
WIDTH = len(board[0])
game_token = [0, 0]
plays = []
while True:

    print('+' + '-' * WIDTH + '+')

    for coordinate_y in range(HEIGHT):
        print('I', end='')

        for coordinate_x in range(WIDTH):

            char = ' '

            for token_plays in plays:
                if token_plays[0] == coordinate_x and token_plays[1] == coordinate_y:
                    char = '#'

            if game_token[0] == coordinate_x and game_token[1] == coordinate_y:
                char = '@'

            if board[coordinate_y][coordinate_x] == '|':
                char = '|'


            print(char, end='')

        print('I')

    print('+' + '-' * WIDTH + '+')

    keys = readchar.readchar()
    new_token = [0, 0]

    if keys == 'd':
        new_token = [(game_token[0] + 2)%14, game_token[1]]
    elif keys == 'a':
        new_token = [(game_token[0] - 2)%14, game_token[1]]
    elif keys == '\n':
        new_token = [game_token[0], game_token[1] + 5]
        if new_token not in plays:
            plays.append(new_token)
        else:
            new_token = [game_token[0], game_token[1] - 1]
            plays.append(new_token)
        new_token = [0, 0]
    elif keys == 'b':
        break

    if new_token:
            game_token = new_token



    os.system("clear")

