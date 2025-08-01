
lista = [4, 2, 6, 8, 5, 7, 0]
# Ordenamiento por seleccion descendente

for iteracion in range(len(lista)):
    minimo = iteracion
    for x in range(iteracion, len(lista)):
        if lista[x] < lista[minimo]:
            minimo = x
    aux = lista[iteracion]
    lista[iteracion] = lista[minimo]
    lista[minimo] = aux

# ascendente

for iteracion in range(len(lista) - 1, 0, -1):
    posicionDelMayor = 0
    for ubicacion in range(1, iteracion + 1):
        if lista[ubicacion] > lista[posicionDelMayor]:
            posicionDelMayor = ubicacion

    temp = lista[iteracion]
    lista[iteracion] = lista[posicionDelMayor]
    lista[posicionDelMayor] = temp
print(lista)