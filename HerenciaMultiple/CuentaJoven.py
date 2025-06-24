from Cuenta import Cuenta


class CrearCuenta(Cuenta):

    def __init__(self, edad, nombre):

        if self.titularValido(edad):
            Cuenta.__init__(self, nombre, edad, 100, valido= True)

        else:
            print("No tienes la edad suficiente")

    def titularValido(self, edad):
        return True if 18 < edad < 25 else False

    def cuenta_joven(self):
        return f"{Cuenta.mostrar()}\n y tu bonus es de 100"

if __name__ == "__main__":

    joven1 = CrearCuenta(20, "Alexis")
    print(joven1.mostrar())
    joven1.ingresar(200)
    print(joven1.mostrar())
    print(joven1.retirar(100))
    print(joven1.mostrar())

    joven2 = CrearCuenta(17, "jorge")
    print(joven2.mostrar())

