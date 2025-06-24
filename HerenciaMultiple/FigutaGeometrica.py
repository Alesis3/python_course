class Figuras:

    def __init__(self, ancho, altura):
        self._ancho = ancho
        self._altura = altura

    def __str__(self):
        return (f"Altura: {self._altura}\n"
                f"Ancho: {self._ancho}")

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura
