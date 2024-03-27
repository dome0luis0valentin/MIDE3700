import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import glob

def graficar(dir):
    file_list = glob.glob(f'/home/valen/PPS/MIDE3700/tests/Suavisar/Output_Suavisar/Teff/*.dat')
    # file_list = dir


    # file_list = glob.glob(f'/home/valen/PPS/MIDE3700/tests/Corregir_teff/*.dat')
    print(file_list)
    x_values = []
    y_values = []
    
    list_curves = []
    
    # Iterate over the files
    valores = []
    for file_path in file_list:
        print(file_path)
        # Open the file and read the coordinates
        with open(file_path, 'r') as f:
            
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
    lista_input = ["CL/Calientes/", "CL/Frias/", "Logg/", "Mbol/", "PHIo/Frias/", "PHIo/Calientes/", "TE/Frias/", "TE/Calientes/", "Mv/", "Teff/"]
    lista_input = ["TE/Calientes/"]
    for dir in lista_input:
        graficar(dir)
    # for dir in paths:
    #     try:
    #         graficar(dir)
    #     except Exception as e:
    #         print(f"Error al cargar la matriz desde el archivo: {e}")
    #         continue

if __name__ == "__main__":
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