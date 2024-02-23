import os
def distancia_euclidea(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def interpolate_values(x1, y1, x2, y2, num_points):
    """
    Interpolate values between two points.
    """
    x_step = (x2 - x1) / (num_points + 1)
    y_step = (y2 - y1) / (num_points + 1)

    interpolated_values = [(x1 + i * x_step, y1 + i * y_step) for i in range(1, num_points + 1)]

    return interpolated_values

def interpolate_files(input_directory, output_directory, dist_promedio):
    """
    Elimina valores que son puntos demasiados cercanos
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Get a list of all .dat files in the input directory
    input_files = [file for file in os.listdir(input_directory) if file.endswith(".dat")]

    lista_distance = []
    for input_file in input_files:
        input_filepath = os.path.join(input_directory, input_file)
        output_filepath = os.path.join(output_directory, input_file)

        with open(input_filepath, 'r') as input_file:
            lines = input_file.readlines()

        with open(output_filepath, 'w') as output_file:
            output_file.write(lines[0])  # Write the header

            primer_valor = lines[1].split()
            x = float(primer_valor[0])
            y = float(primer_valor[1])
            
            output_file.write(f"{x:.5f}     {y:.5f}\n")

            max_distance = 0
            min_distance = 999
            for i in range(1, len(lines)):

            i = 1
            fin_del_archivo = False
            while(i < len(lines)):
                line = lines[i].split()
                
                x1, y1 = float(line[0]), float(line[1])

                if i < len(lines) - 1:
                    next_line = lines[i + 1].split()
                    x2, y2 = float(next_line[0]), float(next_line[1])

                    #Interpolar solo si la distancia euclidea es mayor a cirto punto.
                    
                    distance = distancia_euclidea(x1, y1, x2, y2)
                    if (distance > max_distance):
                        max_distance= distance

                    if (distance < min_distance):
                        print(distance)
                        min_distance = distance 

                    #si los puntos estan demasiado cerca, salte las lineas hasta encontrar uno que este a una distancia correcta
                        
                    #Mientras Distance < error -> Saltar lineas(index++)
                    while (distance < 0.010) and (not fin_del_archivo):
                        i += 1

                        if i < len(lines) - 1:
                            next_line = lines[i + 1].split()
                            x2, y2 = float(next_line[0]), float(next_line[1])

                            #Interpolar solo si la distancia euclidea es mayor a cirto punto.
                            
                            distance = distancia_euclidea(x1, y1, x2, y2)
                        else: 

                        distance = distancia_euclidea(x1, y1, x2, y2)
                else: 
                    fin_del_archivo = True
                i += 1
                output_file.write(f"{x2:.5f}     {y2:.5f}\n")  # Write the last point
        print(f"La maxima distancia euclidea es: {max_distance}\nLa minima distancia euclidea es: {min_distance}")
        lista_distance.append(max_distance)

    return {input_directory: min(lista_distance)}

def main(input_directory, output_directory, num_points):
    interpolate_files(input_directory, output_directory, 2)

if __name__ == "__main__":
    #lista_input = ["CL/Calientes/", "CL/Frias/", "Logg/", "Mbol/", "PHIo/Frias/", "PHIo/Calientes/", "TE/Frias/", "TE/Calientes/", "Mv/", "Teff/"]
    #lista_input = ["Mv/"]
    lista_input = ["Calientes_org/"]
    
    dir_input = "./"
    # dir_input = "./output_relleno_fino/"
    dir_output = "./output_relleno_fino/" 
    
    lista_dic = []
    for case in lista_input:
        input_directory = dir_input+case  # Replace with your input directory
        
        output_directory = dir_output+case  # Replace with your output directory
        num_points = 2  # Number of interpolated points between each pair of rows

        main(input_directory, output_directory, num_points)
