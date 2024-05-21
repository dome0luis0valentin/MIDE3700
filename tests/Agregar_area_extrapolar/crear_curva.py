import numpy as np
import sys
import matplotlib.pyplot as plt

import glob
def procesar_CL_Calientes(curvas):
    """
    Se queda con la mitad de una de las curvas, y para que queden de 50 y 50 puntos,
    se saltean los de la segunda curva, es decir se queda con solo los inidces pares
    """
    curvas[0] = curvas[0][20:70]

    curvas_1= curvas[1]
    curvas[1] = []
    for i in range(0, len(curvas_1)):
        if i % 2 == 0:
            curvas[1].append(curvas_1[i])
    

    return curvas

def procesar_Phio_te(curvas):

    """
    quita los extremos a la segunda curva, y las deja del mismo largo
    """
    # curvas[0] = reversed(curvas[0])
    # curvas[1] = reversed(curvas[1])

    return curvas

def leer_archivos(dir):
    """
    Dado un directorio, con 2 archivos, toma para cada punto de cada archivo y le asigna un valor,
    el valor esta en el header de los archivos y es igual a: min(A,B) + (max(A, B) - min (A, B) / 2)
    """
    valor = -0.5

    file_list = glob.glob(f'/home/valen/PPS/MIDE3700/tests/Agregar_area_extrapolar/Curvas_superiores/{dir}/*.dat')
    print(file_list)
    curvas = []
    values = []

    list_curves = []
    
    # Iterate over the files
    for file_path in file_list:
        if (file_path.endswith("superior.dat")):
            continue
        print(file_path)
        # Open the file and read the coordinates
        with open(file_path, 'r') as f:
            values = []
            for line in f:
                if line.startswith("#"):
                    continue
                else:
                    x = float(line.strip().split()[0])
                    y = float(line.strip().split()[1])
                    values.append((x,y))
            curvas.append(values)
                #Usar

    max_cant = max(len(curvas[0]), len(curvas[1])) 

    curvas[0] = curvas[0][0:max_cant] 
    curvas[1] = curvas[1][0:max_cant]
    

    if dir == "CL/Calientes/":
        procesar_CL_Calientes(curvas)
    if dir == "TE/Frias/":
        procesar_Phio_te(curvas)
    if dir == "PHIo/Frias/" or dir == "Mv/" or dir == "Teff/" or dir == "TE/Calientes/":
        procesar_Phio_te(curvas)
    

    return curvas

def calcular_nuevo_punto_arriba(a, b):
    """
        Dados dos puntos p1, y p2, traza la recta entre ellos, y devuelve un nuevo punto a
        una x-distancia de a.
    """
    x1, y1 = a
    x2, y2 = b

    x_new = x2 + abs(x1-x2)*0.5
    y_new = y2 + abs(y1-y2)*0.5
        
    return x_new, y_new

def calcular_nuevo_punto_abajo(a, b):
    """
        Dados dos puntos p1, y p2, traza la recta entre ellos, y devuelve un nuevo punto a
        una x-distancia de a.
    """
    x1, y1 = a
    x2, y2 = b

    x_new = x2 + abs(x1-x2)*0.5
    y_new = y2 + abs(y1-y2)*0.5
        
    return x_new, y_new

def evaluar(a, b):
    """
    Dados dos puntos, evalua si el punto a esta a la derecha del punto b
    """
    x1, y1 = a
    x2, y2 = b
    if (x1 > x2):
        return False
    else:
        return True

def calcular_nueva_curva(curvas, dir):

    name_file = f'/home/valen/PPS/MIDE3700/tests/Agregar_area_extrapolar/Curvas_superiores/{dir}/superior.dat'
    with open(name_file, 'w') as f:
        i = 0
        for a, b in zip(curvas[0], curvas[1]):
            if (i > 25):
                pass
            evaluación = evaluar(a, b)
            if dir == "CL/Frias/" or dir == "PHIo/Frias/" or dir == "Mbol/" or dir == "TE/Frias/" or dir == "Teff/" or dir == "TE/Calientes/":
                evaluación = not evaluación
            
            if dir == "TE/Calientes/":
                punto_nuevo = calcular_punto_Phio(a, b)
                f.write(f'{punto_nuevo[0]}    {punto_nuevo[1]}\n')
                continue

            if evaluación:
                punto_nuevo = calcular_nuevo_punto_arriba(a, b)
            else:
                punto_nuevo = calcular_nuevo_punto_abajo(a, b)
            i+=1
            f.write(f'{punto_nuevo[0]}    {punto_nuevo[1]}\n')

def calcular_punto_Phio(a, b):
    """
    Dados dos puntos p1, y p2, traza la recta entre ellos, y devuelve un nuevo punto a
    una x-distancia de a.
    """
    x_distancia = 1  # Define la distancia en el eje x
    x1, y1 = a
    x2, y2 = b

    x_new = x2 - abs(x1-x2)*0.5
    y_new = y2 - abs(y1-y2)*0.5
    
    return x_new, y_new

def calcular_nueva_curva_Phio(curvas, dir):
    name_file = f'/home/valen/PPS/MIDE3700/tests/Agregar_area_extrapolar/Curvas_superiores/{dir}/superior.dat'
    with open(name_file, 'w') as f:
        c1 = curvas[1]
        c0 = curvas[0]
        i = 0
        for a, b in zip(c0, c1):
            punto_nuevo = calcular_punto_Phio(a, b)
            
            if False and i == 46 and dir == "PHIo/Calientes/":

                eje_y = 64.1
                for j in range(i, len(c0)):
                    f.write(f'0.078    {eje_y}\n')
                    eje_y += 0.4
                    plt.scatter(a[0], a[1], color='blue', marker='.')
                    plt.scatter(b[0], b[1], color='red', marker='.')
                    plt.scatter(punto_nuevo[0], punto_nuevo[1], color='green', marker='.')
                    plt.draw()
                    plt.pause(0.001)
                break
            
            if i % 100 == 0:
                plt.scatter(a[0], a[1], color='blue', marker='.')
                plt.scatter(b[0], b[1], color='red', marker='.')
                plt.scatter(punto_nuevo[0], punto_nuevo[1], color='green', marker='.')
                plt.draw()
                plt.pause(0.001)
            
            f.write(f'{punto_nuevo[0]}    {punto_nuevo[1]}\n')

            i += 1

    plt.show()  
def main(paths):
    #No tenemos en cuenta las curvas CL, ya que no tienen sentido extrapolar en esos casos.
    lista_input = ["Logg/", "Mbol/", "PHIo/Frias/", "PHIo/Calientes/", "TE/Frias/", "TE/Calientes/", "Mv/", "Teff/"]
    
    c = 2
    lista_input = [lista_input[c]]
    for dir in lista_input:
        curvas = leer_archivos(dir)
      
        # calcular_nueva_curva(curvas, dir)
        calcular_nueva_curva_Phio(curvas, dir)
   
if __name__ == "__main__":
    main([""])

