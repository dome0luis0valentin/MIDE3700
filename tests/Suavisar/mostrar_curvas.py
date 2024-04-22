import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import glob

def graficar(dir):
    # file_list = glob.glob(f'/home/valen/PPS/MIDE3700/{dir}')
    # file_list = dir
    print((f'/home/valen/PPS/MIDE3700/tests/Suavisar/Input_Suavisar{dir}*.dat'))  
    # file_list = glob.glob(f'/home/valen/PPS/MIDE3700/tests/Suavisar/Output_Suavisar/{dir}*.dat')
    file_list = glob.glob(f'/home/valen/PPS/MIDE3700/Curvas/Teff/*.dat')

    x_values = []
    y_values = []
    
    list_curves = []
    
    # Iterate over the files
    valores = []
    print(file_list)
    for file_path in file_list:
        # Open the file and read the coordinates
        print(file_path)
        with open(file_path, 'r') as f:
            
            for line in f:
                if line.startswith("#"):
                    continue
                else:
                    l = list(map(float, line.strip().split()))
                    if len(l) == 2:
                        x, y = map(float, line.strip().split())
                    else:
                        x, y, index= map(float, line.strip().split())
                    x_values.append(x)
                    y_values.append(y)
                    
        # Create a scatter plot
                    
    plt.scatter(x_values, y_values, color='blue', marker='.')  
    plt.show()
    # plt.savefig(f"./Imagenes_Curvas_Sin_Rellenar/{dir.split('/')[-1]}.png") 
    plt.close()
# Ejemplo de uso:
    
def main():
    
    lista_input = ["CL/Calientes/", "CL/Frias/", "Logg/", "Mbol/", "PHIo/Frias/", "PHIo/Calientes/", "TE/Frias/", "TE/Calientes/", "Mv/", "Teff/"]
    lista_input = ["Teff/"]
    for path in lista_input:
        print(path)
        graficar(path)
    
main()