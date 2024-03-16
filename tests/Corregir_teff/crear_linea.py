

def crear_linea(punto_inicio, punto_fin, distancia):
    """
    Crea una línea entre dos puntos.

    Parameters
    ----------
    punto_inicio : tuple
        Coordenadas del punto de inicio.
    punto_fin : tuple
        Coordenadas del punto final.
    distancia : float
        Distancia entre los puntos.

    Returns
    -------
    list
        Lista con las coordenadas de los puntos que forman la línea.
    """
    x1, y1 = punto_inicio
    x2, y2 = punto_fin
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    x = [x1]
    y = [y1]
    if x1 < x2:
        x = [x1 + distancia]
        y = [m * x[0] + b]
        while x[-1] < x2:
            x.append(x[-1] + distancia)
            y.append(m * x[-1] + b)
            
    else:
        x = [x1 - distancia]
        y = [m * x[0] + b]
        while x[-1] > x2:
            x.append(x[-1] - distancia)
            y.append(m * x[-1] + b)
    return list(zip(x, y))

if __name__ == "__main__":
    print("hola")


    punto_inicio = (0.22990, 55.55500)
    punto_fin = (0.23000, 60.70010)
    distancia = 0.000005
    lista = crear_linea(punto_inicio, punto_fin, distancia)

    for i in lista:
        print(f"{i[0]:.5f}     {i[1]:.5f}")
    # [(1, 1), (2, 2), (3, 3), (4, 4)]