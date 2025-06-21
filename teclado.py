from dispEntrada import DispositivosEntrada

class Teclado(DispositivosEntrada):
    contador = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador += 1
        self.id = Teclado.contador
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f"ID:{self.id}.{self.marca}\n"
                f"Tipo de entrad: {self.tipo_entrada}")
