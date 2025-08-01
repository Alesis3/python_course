num_Matrices = int(input("Introduce el numero de matrices a sumar: "))
num_Filas = int(input("Introduce el numero de filas: "))
num_Columnas = int(input("Introduce el numero de columnas: "))

matrices = []
contador = 0


while contador < num_Matrices:
    contador1 = 0
    matrix = []
    while contador1 < num_Filas:
        filas = input(f"Introduce los valores de la fila {contador1} separados por espacios: ")
        newMatrix = filas.split(" ")
        if num_Columnas == len(newMatrix):
            newMatrix = list(map(int, newMatrix))
            matrix.append(newMatrix)
            contador1 += 1
        else:
            print("Ingrese el numero correcto de columnas")
    contador += 1
    matrices.append(matrix)