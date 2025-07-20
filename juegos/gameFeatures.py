def winner(array):
    red_yellow = [[], []]

    for idx, n in enumerate(array):
        if idx % 2 != 0:
            red_yellow[1].append(tuple(n))
        else:
            red_yellow[0].append(tuple(n))

    for idx_partial, turns in enumerate(red_yellow):
        turns_set = set(turns)

        for coordinate_x, coordinate_y in turns:
            # Vertical (misma columna, y consecutivo)
            if all((coordinate_x, coordinate_y + i) in turns_set for i in range(4)):
                return 'Rojos ganan' if idx_partial == 0 else 'Amarillos ganan'

            # Horizontal (misma fila, x consecutivo a la izquierda)
            if all((coordinate_x - 2 * i, coordinate_y) in turns_set for i in range(4)):
                return 'Rojos ganan' if idx_partial == 0 else 'Amarillos ganan'

            # Diagonal ↘ (abajo a la derecha)
            if all((coordinate_x + 2 * i, coordinate_y + i) in turns_set for i in range(4)):
                return 'Rojos ganan' if idx_partial == 0 else 'Amarillos ganan'

            # Diagonal ↙ (abajo a la izquierda)
            if all((coordinate_x - 2 * i, coordinate_y + i) in turns_set for i in range(4)):
                return 'Rojos ganan' if idx_partial == 0 else 'Amarillos ganan'

    return None
