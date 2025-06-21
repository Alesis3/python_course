from computadora import Computador
class ContadorComputadoras:
   contador = 0


   def __init__(self, computador):
       ContadorComputadoras.contador += 1
       self.id = ContadorComputadoras.contador
       self.computador = computador

   def agregar_computadora(self, computador):
       self.computador.append(computador)

   def __str__(self):
       computadora_str = ""
       for computadora in self.computador:
           computadora_str += "\n" + computadora.__str__()

       return (f"ID: {self.id}\n"
               f"Computadoras {computadora_str}")


