"""
Toma a todas las matrices que estan en .np y para cada valor del diccionario le asigna un valor mapeado
El valor mapeado indica en un string, entre que curvas esta el punto
El diccionario tiene el formato: valor -> 2 curvas
    "1.0" : (1.0 ,0.0 )
Rellenar con [c1 c2]
"""
import numpy as np
import os
import matplotlib.pyplot as plt


def mostrar_matriz(matriz):
        fig, ax = plt.subplots()
        # Convert the matrix to a numpy array
        matriz_np = np.array(matriz)

        for i, j in np.ndindex(matriz_np.shape):
            if matriz_np[i, j] == 99999.0:
                matriz_np[i, j] = 0

        # Create a figure and axis
        # fig, ax = plt.subplots()

        # Display the matrix using imshow with intensity-based color mapping
        ax.imshow(matriz_np, cmap='viridis', vmin=np.min(matriz_np), vmax=np.max(matriz_np))

        # # Set the title
        # ax.set_title(titulo)
        
        # Show the plot
        plt.draw()
        plt.show()


dir_input = "./Curvas_Numpy/"

dir_output = "/home/valen/PPS/MIDE3700/tests/Rellenar_curvas_v2/output_nuevas_curvas_np/"

#lee los archivo en un directorio
files = os.listdir(dir_input)
print(files)

for file in files:
    print(file)
    #Read the file
    matriz = np.load(dir_input+file)
    # Map the file
 
    mostrar_matriz(matriz)