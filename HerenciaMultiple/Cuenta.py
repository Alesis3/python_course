
class Cuenta:

    def __init__(self, titular="", edad=0, cantidad=0, valido=False):
        self._edad = edad
        self._titular = titular
        self._cantidad = cantidad
        self._valido = valido

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def edad(self):
        return self._edad


    @property
    def cantidad(self):
        return self._cantidad

    @property
    def valido(self):
        return self._valido

    @valido.setter
    def valido(self, valido):
        self._valido = valido



    def mostrar(self):
        return (f"Titular: {self.titular}\n"
                f"Edad: {self._edad}\n"
                f"Cantidad: {self._cantidad}")

    def ingresar(self, cantidad):

        if cantidad >= 1:
            self._cantidad += cantidad
        else:
            return "Ingresa una cantidad positiva"

        return self._cantidad


    def retirar(self, cantidad=0):

        if self._valido == True :
            self._cantidad -= cantidad
            return cantidad
        else:
            return "Titular invalido"