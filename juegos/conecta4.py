import os
import readchar
from gameFeatures import winner

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
wins = {'Rojos': 0, 'Amarillos': 0}
while True:

    print('+' + '-' * WIDTH + '+')

    for coordinate_y in range(HEIGHT):
        print('I', end='')

        for coordinate_x in range(WIDTH):

            char = ' '

            for idx, token_plays in enumerate(plays):
                if token_plays[0] == coordinate_x and token_plays[1] == coordinate_y:
                    char = 'R' if idx % 2 == 0 else 'A'

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
        new_token = [(game_token[0] + 2) % 14, game_token[1]]

    elif keys == 'a':
        new_token = [(game_token[0] - 2) % 14, game_token[1]]

    elif keys == '\n':
        col = game_token[0]
        for row in range(HEIGHT - 1, -1, -1):
            if [col, row] not in plays:
                plays.append([col, row])
                break
        new_token = [0, 0]

    elif keys == 'b':
        break

    if new_token:
        game_token = new_token

    if len(plays) >= 7:
        answer = winner(plays)
        if answer:
            print(answer)
            input('Presione enter para continuar... ')

            if answer == 'Rojos ganan':
                wins['Rojos'] += 1

            else:
                wins['Amarillos'] += 1
            plays = []
            game_token = [0, 0]

    os.system("clear")
