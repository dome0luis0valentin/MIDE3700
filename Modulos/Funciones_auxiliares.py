from matplotlib.pyplot import gca, draw
import math
import matplotlib.pyplot as plt
import os

def maximizar_pantalla():
    mng = plt.get_current_fig_manager()
    mng.resize(1846,1000)
    return

def distancia_euclidea(x1, x2, y1, y2):
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

def normalize(x, min_val, max_val):
        return (x - min_val) / (max_val - min_val)
    
def desnormalize(x_normalized, min_val, max_val):
    return x_normalized * (max_val - min_val) + min_val

def encontrar_punto_mas_cercano_normalizado(x_norm, y_norm, x_spectro_norm, y_spectro_norm):
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
    x = 0
    y = 0
    closest_spectrum_index = None

    for i in range(len(x_spectro_norm)):
        
        #Multiplico por 10000 a los valores de X para poder calcular las distancias euclideanas de X.
        
        distance = distancia_euclidea(x_spectro_norm[i]*10000, x_norm*10000, y_spectro_norm[i], y_norm)
        if distance < min_distance:
            min_distance = distance
            closest_spectrum_index = i
            x = x_spectro_norm[i]
            y = y_spectro_norm[i]
            
    return x, y

def encontrar_punto_mas_cercano( x_norm, y_norm, x_spectro_norm, y_spectro_norm):
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
    x = 0
    y = 0
    closest_spectrum_index = None

    for i in range(len(x_spectro_norm)):
        
        #Los valores del eje x se multiplican por 10000 para trabajar con valores en una escala aproximada
        
        distance = distancia_euclidea(x_spectro_norm[i]*10000, x_norm*10000, y_spectro_norm[i], y_norm)
        if distance < min_distance:
            min_distance = distance
            closest_spectrum_index = i
            x = x_spectro_norm[i]
            y = y_spectro_norm[i]
            
    #Combierto x e y que estaban normalizados a su verdadera escala
    #x = x_spectro_norm[closest_spectrum_index] 
    #y = y_spectro_norm[closest_spectrum_index] 
        
    return x, y

def calcular_indice_del_punto_mas_cercano_normalizado(clic_x, clic_y, coor_x, coor_y):
    # Inicializa la distancia mínima como infinito y el índice del punto más cercano como -1
    distancia_minima = float('inf')
    indice_mas_cercano = -1
    
    # Itera a través de las coordenadas x e y para encontrar el punto más cercano
    for i in range(len(coor_x)):
        
        #Multiplico por 10000 para tratar con valores con una escala aproximada
        distancia = math.sqrt((clic_x*10000 - coor_x[i]*10000) ** 2 + (clic_y - coor_y[i]) ** 2)
        if distancia < distancia_minima:
            distancia_minima = distancia
            indice_mas_cercano = i
    
    # Devuelve el índice del punto más cercano
    return indice_mas_cercano



def calcular_indice_del_punto_mas_cercano(clic_x, clic_y, coor_x, coor_y):
    # Inicializa la distancia mínima como infinito y el índice del punto más cercano como -1
    distancia_minima = float('inf')
    indice_mas_cercano = -1
    
    # Itera a través de las coordenadas x e y para encontrar el punto más cercano
    for i in range(len(coor_x)):
        distancia = math.sqrt((clic_x - coor_x[i]) ** 2 + (clic_y - coor_y[i]) ** 2)
        if distancia < distancia_minima:
            distancia_minima = distancia
            indice_mas_cercano = i
    
    # Devuelve el índice del punto más cercano
    return indice_mas_cercano