import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import glob

def graficar(dir):
    # file_list = glob.glob(f'/home/valen/PPS/MIDE3700/{dir}')
    # file_list = dir


    file_list = glob.glob(f'/home/valen/PPS/MIDE3700/tests/Agregar_area_extrapolar/Curvas_superiores/{dir}/*.dat')
    # file_list = glob.glob(f'/home/valen/PPS/MIDE3700/Curvas/{dir}/*.dat')
    print(file_list)
    x_values = []
    y_values = []
    x_new = []
    y_new = []
    
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
                    if (file_path.endswith("rior.dat")):
                        x = float(line.strip().split()[0])
                        y = float(line.strip().split()[1])
                        x_new.append(x)
                        y_new.append(y)

                    else:
                        x = float(line.strip().split()[0])
                        y = float(line.strip().split()[1])
                        x_values.append(x)
                        y_values.append(y)
                    
        # Create a scatter plot
    
  
    plt.scatter(x_values, y_values, color='blue', marker='.') 
    plt.scatter(x_new, y_new, color='red', marker='.') 
    plt.show()
    # plt.savefig(f"./Imagenes_Curvas_Sin_Rellenar/{dir.split('/')[-1]}.png") 
    plt.close()
# Ejemplo de uso:
    
def main(paths):
    # lista_input = ["CL/Calientes/", "CL/Frias/", "Logg/", "Mbol/", "PHIo/Frias/", "PHIo/Calientes/", "TE/Frias/", "TE/Calientes/", "Mv/", "Teff/"]
    lista_input = ["Logg/", "Mbol/", "PHIo/Frias/", "PHIo/Calientes/", "TE/Frias/", "TE/Calientes/", "Mv/", "Teff/"]
    c = 7
    lista_input = [lista_input[c]]

    for dir in lista_input:
        graficar(dir)
  

if __name__ == "__main__":
    main([""])
