def calcular_nuevo_punto(a, b):
    """
        Dados dos puntos p1, y p2, traza la recta entre ellos, y devuelve un nuevo punto a
        una x-distancia de a.
    """
    x_distancia = 1  # Define la distancia en el eje x
    x1, y1 = a
    x2, y2 = b

    if ( x1 == x2):
        m = 1
        return x1, min(y1, y2)-abs(y2-y1)
    else:
        m = (y2 - y1) / (x2 - x1)  # Calcula la pendiente de la recta

    b = -(x1 * m) + y1
    x_new = x2 + 1 / ((1 + m ** 2) ** 0.5)
    y_new = y2 + m * (x_new - x2)

    return x_new, y_new

   
puntos = [(0, 1), (1,1), (1,0), (-1, 1)]
for p in puntos:
    print(calcular_nuevo_punto((0,0), p))