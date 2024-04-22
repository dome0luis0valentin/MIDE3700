import os
from math import dist

def distancia_euclidea(x1, y1, x2, y2):
    a = (x1*100, y1)
    b = (x2*100, y2)

    return dist(a, b)

def calcular_distancia_segmento(lines):
    """
    Tomo una muestra de elementos del segmento para lograr una distancia aproximada
    """
    
    if (lines[0].startswith("#")):
        lines.pop(0)
    distancia_total = 0

    for i in range(len(lines)-1):
        primer = lines[i].split()
        sig = lines[i + 1].split()

        x1 = float(primer[0])
        x2 = float(sig[0])
        y1 = float(primer[1])
        y2 = float(sig[1])

        distancia_total += distancia_euclidea(x1, y1, x2, y2)

    return distancia_total

def calc_distance_points(p1, p2):
    return distancia_euclidea(p1[0], p1[1], p2[0], p2[1])

def leer_punto(lines, index):
    valor =lines[index].split()
    x = float(valor[0])
    y = float(valor[1])

    return(x, y)

def suavisar(input_directory, dir_out):
    """
    Esta función, toma los archivos .dat de un directorio, que contienen un conjunto de puntos que forman una curva
    y crea otro archivo pero con menos puntos, pero representan la misma curva
    """
    # Create the output directory if it doesn't exist
    os.makedirs(dir_out, exist_ok=True)

    # Get a list of all .dat files in the input directory
    input_files = [file for file in os.listdir(input_directory) if file.endswith(".dat")]


    for input_file in input_files:
        input_filepath = os.path.join(input_directory, input_file)
        output_filepath = os.path.join(output_directory, input_file)
        
        cant_lines = 0

        with open(input_filepath, 'r') as input_file:
            lines = input_file.readlines()

        with open(output_filepath, 'w') as output_file:
            output_file.write(lines[0])  # Write the header

            #Escribe el primer valor del archivo
            primer_valor = lines[1].split()
            x = float(primer_valor[0])
            y = float(primer_valor[1])
            output_file.write(f"{x:.5f}     {y:.5f}     {0}\n")

            distance = calcular_distancia_segmento(lines)

            #Recorremos cada archivo, y cada vez que superamos la distancia marcamos un punto
            segment_distance = distance/100
            
            index = 2
            punto_actual = (x, y)
            punto_siguiente = leer_punto(lines, index)

            while (index+1 < len(lines)):

                distance_points = calc_distance_points(punto_actual, punto_siguiente)
                while (distance_points < segment_distance) and (index+1 < len(lines)) :
                    index += 1
                    punto_siguiente = leer_punto(lines, index)
                    distance_points = calc_distance_points(punto_actual, punto_siguiente)

                #Escribo el punto en la salida
                output_file.write(f"{punto_siguiente[0]:.5f}     {punto_siguiente[1]:.5f}     {index}\n")

                cant_lines += 1

                #Actualizo el punto de referencia para comparar distancias
                punto_actual = punto_siguiente

        print("Largo final del archivo: ", cant_lines)

if __name__ == "__main__":
    lista_input = ["CL/Calientes/", "CL/Frias/", "Logg/", "Mbol/", "PHIo/Frias/", "PHIo/Calientes/", "TE/Frias/", "TE/Calientes/", "Mv/", "Teff/"]
    
    # dir_input = "./"
    dir_input = "./Input_Suavisar/Curvas/"
    dir_output = "./Output_Suavisar/" 
    
    lista_dic = []
    for case in lista_input:
        print("Case ", case)

        input_directory = dir_input+case  
        output_directory = dir_output+case  # Replace with your output directory
        
        suavisar(input_directory, output_directory)