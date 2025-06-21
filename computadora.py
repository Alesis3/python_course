

class Computador:
    contador = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computador.contador += 1
        self.id = Computador.contador
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''{self.nombre}: {self.id}
        Monitor: {self.monitor}.
        Teclado: {self.teclado}=
        Raton: {self.raton}"'''

