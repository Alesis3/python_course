lista = [4, 2, 6, 8, 5, 7, 0]

for indice in range(1, len(lista)):

    valorActual = lista[indice]
    posicion = indice

    while posicion > 0 and lista[posicion - 1] > valorActual:
        lista[posicion] = lista[posicion - 1]
        posicion = posicion - 1

    lista[posicion] = valorActual 