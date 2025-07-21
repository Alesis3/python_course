import os
import readchar
from gameFeatures import winner, reset

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

    # Imprime el tablero, posicion y jugadas
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
    print(f'VICTORIAS'.center(WIDTH, '*'))
    print(f"Rojos: {wins['Rojos']} Amarillos: {wins['Amarillos']}")
    # Funciones del juego al interactuar desde teclado

    keys = readchar.readchar()
    new_token = [0, 0]

    if keys == 'd':
        new_token = [(game_token[0] + 2) % 14, game_token[1]]

    elif keys == 'a':
        new_token = [(game_token[0] - 2) % 14, game_token[1]]

    elif keys == '\n':
        # Colocación de fichas
        col = game_token[0]
        for row in range(HEIGHT - 1, -1, -1):
            if [col, row] not in plays:
                plays.append([col, row])
                break
        new_token = [0, 0]
    elif keys == 'r':
        # Funcion de resetear partida o juego
        user = input('Resetear partida [p]\n'
                     'Resetear juego [j]')
        if user == 'p':
            plays, new_token = reset(plays, new_token)
        elif user == 'j':
            plays, new_token = reset(plays, new_token)
            wins = {clave: 0 for clave in wins}
        else:
            print('Elige una opción valida')

    elif keys == 'b':
        break
    # Funcion para saber los ganadores
    if len(plays) >= 7:
        answer = winner(plays)
        if answer:
            print(answer)
            input('Presione enter para continuar... ')

            if answer == 'Rojos ganan':
                wins['Rojos'] += 1

            else:
                wins['Amarillos'] += 1
            plays, new_token = reset(plays, new_token)

    if new_token:
        game_token = new_token

    os.system("clear")
