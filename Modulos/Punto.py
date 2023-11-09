import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class Punto(Circle):
    #Por defecto siempre van a tener el mismo tamaño y color verde
    def __init__(self, x, y,  color='green', radius=0.01 ,activate=True, *args, **kwargs):
        super().__init__((x, y), radius, color=color, *args, **kwargs)
        self.x = x
        self.y = y
        self.activate = activate

    def set_activate(self, activate):
        self.activate = activate

    def get_activate(self):
        return self.activate