import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import glob

def graficar(dir):
    # file_list = glob.glob(f'/home/valen/PPS/MIDE3700/{dir}')
    file_list = dir


# file_list = glob.glob(f'/home/valen/pps/MIDE3700_v2/MIDE3700/Curvas/{dir}/*.dat')

    x_values = []
    y_values = []
    
    list_curves = []
    
    # Iterate over the files
    valores = []
    for file_path in file_list:
        # Open the file and read the coordinates
        with open("/home/valen/PPS/MIDE3700/"+file_path, 'r') as f:
            
            for line in f:
                if line.startswith("#"):
                    continue
                else:
                    x, y = map(float, line.strip().split())
                    x_values.append(x)
                    y_values.append(y)
                    
        # Create a scatter plot
                    
    plt.scatter(x_values, y_values, color='blue', marker='.')  
    plt.show()
    # plt.savefig(f"./Imagenes_Curvas_Sin_Rellenar/{dir.split('/')[-1]}.png") 
    plt.close()
# Ejemplo de uso:
    
def main(paths):
    path = glob.glob(f'/home/valen/PPS/MIDE3700/')

    print("Estos son los paths = ", paths)
    graficar(paths)
    # for dir in paths:
    #     try:
    #         graficar(dir)
    #     except Exception as e:
    #         print(f"Error al cargar la matriz desde el archivo: {e}")
    #         continue

if __name__ == "main":
    main([""])


#Checkea si hay otro directorio dentro

# for file in path:
#     matriz_resultante = cargar_matriz_desde_archivo(file)
#     matriz_resultante[matriz_resultante == 99999.0] = 0
#     plt.matshow(matriz_resultante)
#     plt.savefig(f'./Imagenes_Curvas_Rellenas/{file.split("/")[-1].split(".")[0]}.png')
#     plt.draw()

# matriz_resultante = cargar_matriz_desde_archivo("/home/valen/PPS/MIDE3700/tests/Curvas_en_text/TE-Frias.txt")
# #Reemplazar 99999.9 por 0
# matriz_resultante[matriz_resultante == 99999.0] = 0

# plt.matshow(matriz_resultante)
# plt.show()