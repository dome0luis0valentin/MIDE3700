import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import glob
import numpy as np

def colorear_horizontal(matriz):
    ancho_matriz = matriz.shape[1]-1
        
    vacio = 99999.0
    valor_actual = vacio
        
    for fila in matriz:
        index = 0
            
        #busco el primer punto de la curva
        while (fila[index] == vacio and index < ancho_matriz):
            index += 1
                    
            #relleno con ese valor hasta la próxima curva
        valor_actual = fila[index]
                        
            #no se termine la matriz
        while (index < ancho_matriz):
                
                #no llegue a otra curva
            while ( (fila[index] == vacio or fila[index] == valor_actual )and index < ancho_matriz):
                fila[index] = valor_actual
                index += 1
                    
                #cambio al nuevo valor de la curva
            valor_actual = fila[index]

def colorear_horizontal_inverso(matriz):
    ancho_matriz = matriz.shape[1]-1
        
    vacio = 99999.0
    valor_actual = vacio
        
    for fila in matriz:
        index = ancho_matriz
            
        #busco el primer punto de la curva
        while (fila[index] == vacio and index > 0):
            index -= 1
                    
            #relleno con ese valor hasta la próxima curva
        valor_actual = fila[index]
                        
            #no se termine la matriz
        while (index > 0):
                
                #no llegue a otra curva
            while ( (fila[index] == vacio or fila[index] == valor_actual )and index > 0):
                fila[index] = valor_actual
                index -= 1
                    
                #cambio al nuevo valor de la curva
            valor_actual = fila[index]
    
def colorear_vertical(matriz):

    ancho_matriz = matriz.shape[1]
    alto_matriz = len(matriz)-1
        
    vacio = 99999.0
    valor_actual = vacio
        
    for col in range(ancho_matriz):
        index = 0
            
        # busco el primer punto de la curva
        while (matriz[index][col] == vacio and index < alto_matriz):
                index += 1
                    
        # relleno con ese valor hasta la próxima curva
        valor_actual = matriz[index][col]
            
        # no se termine la matriz
        while (index < alto_matriz):
                
            # no llegue a otra curva
            while ((matriz[index][col] == vacio or matriz[index][col] == valor_actual) and index < alto_matriz):
                matriz[index][col] = valor_actual
                index += 1
                    
            # cambio al nuevo valor de la curva
            if index < alto_matriz:
                valor_actual = matriz[index][col]

def colorear_vertical_inverso(matriz):

    ancho_matriz = matriz.shape[1]
    alto_matriz = len(matriz)-1
        
    vacio = 99999.0
    valor_actual = vacio
        
    for col in range(ancho_matriz):
        index = alto_matriz
            
        # busco el primer punto de la curva
        while (matriz[index][col] == vacio and index > 0):
                index -= 1
                    
        # relleno con ese valor hasta la próxima curva
        valor_actual = matriz[index][col]
            
        # no se termine la matriz
        while (index > 0):
                
            # no llegue a otra curva
            while ((matriz[index][col] == vacio or matriz[index][col] == valor_actual) and index > 0):
                matriz[index][col] = valor_actual
                index -= 1
                    
            # cambio al nuevo valor de la curva
            if index > 0:
                valor_actual = matriz[index][col]

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

path = glob.glob(f'../Curvas_Numpy/*')
for numpy_file in path:

    #Cargar Matriz
    matriz_numpy = np.load(numpy_file)
    print(numpy_file)
    # Corregirla
    # if (numpy_file == "./Curvas_Numpy/TE-Calientes.npy"):
    #     colorear_vertical_inverso(matriz_numpy)
    # elif(numpy_file == "./Curvas_Numpy/Mbol.npy"):
    #     colorear_vertical(matriz_numpy)
    # elif(numpy_file == "./Curvas_Numpy/PHIo-Calientes.npy"):
    #     colorear_horizontal_inverso(matriz_numpy)
    # elif(numpy_file == "./Curvas_Numpy/CL-Frias.npy"):
    #     pass

    # Guardarla 
    # np.save(f'./output/{numpy_file.split("/")[-1].split(".")[0]}.npy', matriz_numpy)   

    #Mostrarla
    if numpy_file.split("/")[-1].split(".")[0] == "Logg":
        matriz_numpy[matriz_numpy == 99999.0] = 1   
    else:
        matriz_numpy[matriz_numpy == 99999.0] = 0

    # Guarda la matriz en una imagen
    print(numpy_file.split("/")[-1].split(".")[0])
    plt.matshow(matriz_numpy)
    
    
    
    plt.show()
    # plt.savefig(f'./Imagenes_Curvas_Rellenas_Cuadradas/{numpy_file.split("/")[-1].split(".")[0]}.png')
    # plt.close()   
# matriz_resultante = cargar_matriz_desde_archivo("/home/valen/PPS/MIDE3700/tests/Curvas_en_text/TE-Frias.txt")
# #Reemplazar 99999.9 por 0
# matriz_resultante[matriz_resultante == 99999.0] = 0

# plt.matshow(matriz_resultante)
# plt.show()