def mostrar_inventario():
    for producto in inventario:
        print(
            f"Id: {producto["id"]}. Nombre: {producto["nombre"]}. Precio: {producto["precio"]}. Cantidad: {producto["cantidad"]}")

def agregar_prod():
    id = len(inventario) + 1
    nombre = input("Ingrese el producto: ")
    precio = int(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    inventario.append({"id": id, "nombre": nombre, "precio": precio, "cantidad": cantidad})
    print("Se agrego con exito el producto")

def buscar_id():
    id = int(input("Introduce el ID del producto: "))

    for id_inventario in inventario:

        if id_inventario["id"] == id:
            print(f"Id: {id_inventario["id"]}. Nombre: {id_inventario["nombre"]}. "
                  f"Precio: {id_inventario["precio"]}. Cantidad: {id_inventario["cantidad"]}")
        else:
            continue

inventario = [{"id": 1, "nombre": "Camisa", "precio": 20, "cantidad": 12},
              {"id": 2, "nombre": "Pantalon", "precio": 30, "cantidad": 5}]

while True:
    user = int(input("1.Mostrar inventario \n"
                     "2.Agregar producto \n"
                     "3.Buscar por ID \n"
                     "4.Salir \n"
                     "Introduce una opcion: "))
    if user == 1:
        mostrar_inventario()

    elif user == 2:
        agregar_prod()

    elif user == 3:
        buscar_id()

    elif user == 4:
        break
    else:
        print("Introduce un valor correcto: ")