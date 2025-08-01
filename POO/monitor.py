

class Monitor:
    contador = 0

    def __init__(self, marca, tamanio):
        Monitor.contador += 1
        self .id = Monitor.contador
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return (f"\n ID:{self.id}.{self.marca}\n"
                f"Tamaño: {self.tamanio}")