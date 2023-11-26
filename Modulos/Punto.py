import matplotlib.pyplot as plt

class Punto:
    #Por defecto siempre van a tener el mismo tamaño y color verde
    def __init__(self, x, y, grafico, color='red', activate=True ):
        self.x = x
        self.y = y
        self.activate = activate
        self.grafico = grafico

    def set_activate(self, activate):
        self.activate = activate

    def get_activate(self):
        return self.activate
    
    def set_color(self, color):
        print("Cambiando el color: ", color, " Grafico es d e tipo: ", type(self.grafico), " es ", self.grafico)
        
        self.grafico.set_color(color)