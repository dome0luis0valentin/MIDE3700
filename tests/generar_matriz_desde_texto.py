import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import glob
import numpy as np

def cargar_matriz_desde_archivo(archivo):
    try:
        # Cargar el archivo como matriz de strings
        with open(archivo, 'r') as f:
            lineas = f.readlines()

        # Separar las celdas por espacios en blanco y convertir a números
        matriz = np.array([list(map(float, linea.split(",")))
                          for linea in lineas])

        return matriz

    except Exception as e:
        print(f"Error al cargar la matriz desde el archivo: {e}")
        return None

def matrices_son_iguales(matriz1, matriz2):
    # Verificar si las dimensiones de las matrices son iguales
    if matriz1.shape != matriz2.shape:
        return False

    # Comparar celda por celda
    comparacion_celda = np.equal(matriz1, matriz2)

    # Verificar si todas las celdas son iguales
    son_iguales = np.all(comparacion_celda)

    return son_iguales

# Ejemplo de uso:

path = glob.glob(f'./Curvas_en_text/TE*')
for file in path:
    matriz_resultante = cargar_matriz_desde_archivo(file)
    if file.split("/")[-1].split(".")[0] == "Logg":
        matriz_resultante[matriz_resultante == 99999.0] = 1
        # plt.matshow(matriz_resultante)
        # plt.show()    
    else:
        matriz_resultante[matriz_resultante == 99999.0] = 0
    np.save(f'./Matrices_Numpy/{file.split("/")[-1].split(".")[0]}.npy', matriz_resultante)

    # Guarda la matriz en una imagen
    print(file.split("/")[-1].split(".")[0])
    
    plt.matshow(matriz_resultante)
    
    plt.show()
    plt.savefig(f'./Imagenes_Curvas_Rellenas/{file.split("/")[-1].split(".")[0]}.png')
    plt.close()   
# matriz_resultante = cargar_matriz_desde_archivo("/home/valen/PPS/MIDE3700/tests/Curvas_en_text/TE-Frias.txt")
# #Reemplazar 99999.9 por 0
# matriz_resultante[matriz_resultante == 99999.0] = 0

# plt.matshow(matriz_resultante)
# plt.show()