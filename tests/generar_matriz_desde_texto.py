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
archivo_ejemplo = './Curvas_en_text/CL-Calientes.txt'
matriz_resultante = cargar_matriz_desde_archivo(archivo_ejemplo)

if matriz_resultante is not None:
    print("Matriz cargada:")
    print(matriz_resultante)
