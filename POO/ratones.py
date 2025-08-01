from dispEntrada import DispositivosEntrada

class Ratones(DispositivosEntrada):
    contador =  0

    def __init__(self, marca, tipo_entrada):
        Ratones.contador += 1
        self.id = Ratones.contador
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f"ID{self.id}. Marca: {self.marca} \n "
                f"Tipo de entrada: {self.tipo_entrada}")



