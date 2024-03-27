from matplotlib.pyplot import gca, draw
import math
import matplotlib.pyplot as plt
import os

#https://stackoverflow.com/questions/2049582/how-to-determine-if-a-point-is-in-a-2d-triangle
def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1]);

def point_in_triangle(pt, v1, v2, v3):
    d1 = (0,0)
    d2 = (0,0)
    d3 = (0,0)
    has_neg = False
    has_pos = False

    d1 = sign(pt, v1, v2);
    d2 = sign(pt, v2, v3);
    d3 = sign(pt, v3, v1);

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0);
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0);

    return not (has_neg and has_pos)

def calcular_min_distance(xy, curva):
    min_distance = float("inf")
    min_point = (0, 0)
    # print("Punto a buscar ",xy)
    for punto in curva:
        
        distance = distancia_euclidea_v2(xy[0], punto[0], xy[1], punto[1])
        if distance < min_distance:
            min_point = punto
            min_distance = distance

    # output = open("/home/valen/PPS/MIDE3700/tests/resultados_interpolación/resultados.txt", "a")
    # output.write(f"# {xy[0]} {xy[1]} {min_point[0]} {min_point[1]}\n")
    # output.write(f"{min_distance}\n")
    # output.close()

    # print("El punto más cercano esta en la posición: ",min_point[0], min_point[1])
    plt.scatter(x = min_point[0], y = min_point[1], c = "black", marker = "o", s = 100)
    
    return min_distance

def maximizar_pantalla():
    mng = plt.get_current_fig_manager()
    mng.resize(1846,1000)
    return

def distancia_euclidea_v2(x1, x2, y1, y2):
    di = ((x1 - x2) ** 2)
    dj = ((y1 - y2) ** 2)
    
    return math.sqrt( di + dj )

    d1 = math.sqrt((x1 - x2) ** 2)

    d2 = math.sqrt((y1 - y2) ** 2)
    print(x1, y1, x2, y2)
    print(f"d1: {d1}")
    print(f"d2: {d2}")

    dist = (d1) + (d2)
    print(dist)
    return dist
    
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

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