from matplotlib.pyplot import gca, draw
import math


def distancia_euclidea(x1, x2, y1, y2):
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


def encontrar_punto_mas_cercano( x_clicked, y_clicked, x_spectro_norm, y_spectro_norm, max_x_spectrum, max_y_spectrum):
    """
    Encuentra el punto más cercano en el espectro a las coordenadas (x_clicked, y_clicked).

    :param x_spectrum: Lista de coordenadas x del espectro Normalizado entre 0 y 1
    :param y_spectrum: Lista de coordenadas y del espectro Normalizado entre 0 y 1
    :param x_clicked: Coordenada x del clic.
    :param y_clicked: Coordenada y del clic.
    :param max_x_spectrum: Es el máximo valor del espectro en x
    :param max_y_spectrum: Es el máximo valor del espectro en y
    :return: Coordenadas x e y del espectro al punto más cercano
    """
    min_distance = float("inf")
    closest_spectrum_index = None
    
    for i in range(len(x_spectro_norm)):
        distance = distancia_euclidea(x_spectro_norm[i], x_clicked/ max_x_spectrum, y_spectro_norm[i]/ max_y_spectrum, y_clicked/ max_y_spectrum)
        if distance < min_distance:
            min_distance = distance
            closest_spectrum_index = i
        #print(i, distance)
    #print("MInima distancia con i = ", closest_spectrum_index)
    
    #Combierto x e y que estaban normalizados a su verdadera escala
    x = x_spectro_norm[closest_spectrum_index] * max_x_spectrum
    y = y_spectro_norm[closest_spectrum_index] * max_y_spectrum
    
    return x, y