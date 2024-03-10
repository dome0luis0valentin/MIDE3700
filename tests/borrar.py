import matplotlib.pyplot as plt
import numpy as np  # Importamos numpy para generar colores aleatorios

# Datos iniciales
x_values = []
y_values = []

# Función para agregar puntos con color y forma personalizados
def agregar_punto(x, y, color='blue', marker='o'):
    x_values.append(x)
    y_values.append(y)
    actualizar_grafico(color, marker)

# Función para actualizar el gráfico
def actualizar_grafico(color, marker):
    plt.scatter(x_values, y_values, color=color, marker=marker)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Gráfico en tiempo real')
    plt.show()

# Ejemplo de uso
agregar_punto(1, 2, color='red', marker='o')
agregar_punto(2, 4, color='green', marker='^')
agregar_punto(3, 1, color='blue', marker='s')

plt.scatter(x_values, y_values, color='red', marker='o')
plt.scatter([1, 2, 3], [1, 2, 3], color='red', marker='x', label='Nuevos puntos')
plt.show()
# Puedes seguir llamando a agregar_punto para agregar más puntos iterativamente