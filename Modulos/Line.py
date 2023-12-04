import matplotlib.pyplot as plt

class Line:
    #Por defecto siempre van a tener el mismo tamaño y color verde
    def __init__(self, grafico, color='green', last=True ):
        self.last = last
        self.color_original = grafico.get_color()
        self.grafico = grafico

    def set_last(self, activate):
        self.last = activate

    def is_last(self):
        return self.last
    
    def set_color(self, color):
        print("Cambiando el color: ", color, " Grafico es d e tipo: ", type(self.grafico), " es ", self.grafico)
        
        self.grafico.set_color(color)
        
    def get_color(self):
        return self.grafico.get_color()
    
    def get_color_original(self):
        return self.color_original