from FigutaGeometrica import Figuras
from Color import Color


class Cuadrado(Figuras, Color):

    def __init__(self, lado, color):
        Figuras.__init__(self, lado, lado)
        Color.__init__(self, color)

    def __str__(self):
        return f"{Figuras.__str__(self)}, {Color.__str__(self)}"

    def area(self):
        return self.ancho * self.altura
