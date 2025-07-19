
plays = [[1,3],[2,3],[4,5], [4,2],[9,8],[2,4], [5,3],[2,5],[7,4], [2,6]]
"""
def ganador(lista):
    rojos_amarillos = [[],[]]

    for idx, n in enumerate(lista):
        if idx % 2 != 0:
            rojos_amarillos[1].append(n)
        else:
            rojos_amarillos[0].append(n)


    for m in rojos_amarillos:
        contador = 1
        player_moves = sorted(m)
        jugada_anterior = player_moves[0]

        for jugada in player_moves[1:]:
            if contador == 4:
                break
            else:
                if jugada[0] == jugada_anterior[0] and jugada[1] == jugada_anterior[1] + 1:
                    contador += 1
                    jugada_anterior = jugada

                elif jugada[1] == jugada_anterior[1] and jugada[0] == jugada_anterior[0] - 1:
                    contador += 1
                    jugada_anterior = jugada

                else:
                    jugada_anterior = jugada
                    contador = 1

        if m == rojos_amarillos[0] and contador == 4:
            return 'Rojos Ganan'
        elif m == rojos_amarillos[1] and contador == 4:
            return 'Amarillos ganan'
        else:
            pass
"""

plays = [[1,3],[2,3],[4,5], [4,2],[9,8],[2,4], [5,3],[2,5],[7,4], [2,6]]

def ganador(lista):
    rojos_amarillos = [[], []]

    for idx, n in enumerate(lista):
        if idx % 2 != 0:
            rojos_amarillos[1].append(tuple(n))
        else:
            rojos_amarillos[0].append(tuple(n))

    for i, jugadas in enumerate(rojos_amarillos):
        jugadas_set = set(jugadas)

        for x, y in jugadas:
            # Vertical (misma columna, y consecutivo)
            if all((x, y + i) in jugadas_set for i in range(4)):
                return 'Rojos ganan' if i == 0 else 'Amarillos ganan'

            # Horizontal (misma fila, x consecutivo a la izquierda)
            if all((x - i, y) in jugadas_set for i in range(4)):
                return 'Rojos ganan' if i == 0 else 'Amarillos ganan'

            # Diagonal ↘ (abajo a la derecha)
            if all((x + i, y + i) in jugadas_set for i in range(4)):
                return 'Rojos ganan' if i == 0 else 'Amarillos ganan'

            # Diagonal ↙ (abajo a la izquierda)
            if all((x - i, y + i) in jugadas_set for i in range(4)):
                return 'Rojos ganan' if i == 0 else 'Amarillos ganan'

    return 'Nadie gana'


if __name__ == '__main__':
    print(ganador(plays))

