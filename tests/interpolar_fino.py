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
    Interpolate values between two points for all .dat files in the input directory.
    Save the interpolated files in the output directory.
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

            #Para cada linea, que contiene un punto.
            for i in range(1, len(lines)):
                line = lines[i].split()
                
                x1, y1 = float(line[0]), float(line[1])

                if i < len(lines) - 1:
                    next_line = lines[i + 1].split()
                    x2, y2 = float(next_line[0]), float(next_line[1])

                    #Interpolar solo si la distancia euclidea es mayor a cirto punto.
                    
                    distance = distancia_euclidea(x1, y1, x2, y2)
                    if (distance >= max_distance):
                        max_distance= distance
# and (27 < y1 < 40 or 48 <= y1 <=51 or 55 <= y1 <=56 or 68 <= y1 <= 69 or 74 <= y1 <= 75 or 81 <= y1 <= 82 or 87 <= y1 <= 88)
                    if (distance > dist_promedio) :
                        num_puntos = int(distance/dist_promedio)
                        # num_puntos = 10
                        interpolated_values = interpolate_values(x1, y1, x2, y2, num_puntos)

                        for x, y in interpolated_values:
                            output_file.write(f"{x:.5f}     {y:.5f}\n")

                output_file.write(f"{x2:.5f}     {y2:.5f}\n")  # Write the last point
        print(f"Archivo: {input_file.name} \nLa maxima distancia euclidea es: {max_distance}")
        lista_distance.append(max_distance)

    # d = {input_directory: min(lista_distance)}
    # print(d)
    return None
    print(f"La maxima distancia euclidea es: {min(lista_distance)}, el promedio: {sum(lista_distance)/len(lista_distance)}")

def main(input_directory, output_directory, num_points):
    # lista = {'./Agregar_area_extrapolar/Curvas_superiores/CL/Calientes/': 0.007100345062038695,'./Agregar_area_extrapolar/Curvas_superiores/CL/Frias/': 0.005900415239621998,'./Agregar_area_extrapolar/Curvas_superiores/Logg/': 0.610721294863706,'./Agregar_area_extrapolar/Curvas_superiores/Mbol/': 0.11600002112068739,'./Agregar_area_extrapolar/Curvas_superiores/PHIo/Frias/': 0.028140063965805553,'./Agregar_area_extrapolar/Curvas_superiores/PHIo/Calientes/': 0.10437002347417872,'./Agregar_area_extrapolar/Curvas_superiores/TE/Frias/': 0.028140063965805553,'./Agregar_area_extrapolar/Curvas_superiores/TE/Calientes/': 0.10437002347417872,'./Agregar_area_extrapolar/Curvas_superiores/Mv/': 0.05150004757279788,'./Agregar_area_extrapolar/Curvas_superiores/Teff/': 0.10667002296803092}
    
    #Curvas externas
    lista = {'./Agregar_area_extrapolar/Curvas_superiores/CL/Calientes/': 0.007100345062038695,'./Agregar_area_extrapolar/Curvas_superiores/CL/Frias/': 0.005900415239621998,'./Agregar_area_extrapolar/Curvas_superiores/Logg/': 0.004970492933301626,'./Agregar_area_extrapolar/Curvas_superiores/Mbol/': 0.0011600002112068739,'./Agregar_area_extrapolar/Curvas_superiores/PHIo/Frias/': 0.0958140063965805553,'./Agregar_area_extrapolar/Curvas_superiores/PHIo/Calientes/': 0.01437002347417872,'./Agregar_area_extrapolar/Curvas_superiores/TE/Frias/': 0.028140063965805553,'./Agregar_area_extrapolar/Curvas_superiores/TE/Calientes/': 0.10437002347417872,'./Agregar_area_extrapolar/Curvas_superiores/Mv/': 0.05150004757279788,'./Agregar_area_extrapolar/Curvas_superiores/Teff/': 0.10667002296803092}
    lista = {"./input_Curvas_Interpolar/" : 0.005}
    
    return interpolate_files(input_directory, output_directory, lista[input_directory])

if __name__ == "__main__":
    # lista_input = ["CL/Calientes/", "CL/Frias/", "Logg/", "Mbol/", "PHIo/Frias/", "PHIo/Calientes/", "TE/Frias/", "TE/Calientes/", "Mv/", "Teff/"]
    lista_input = ["/"]
    # c = 2

    # lista_input = lista_input[3:11]
    # dir_input = "./Agregar_area_extrapolar/Curvas_superiores/"
    dir_input = "./input_Curvas_Interpolar/"
    # dir_input = "./output_relleno_fino/"
    dir_output = "./Agregar_area_extrapolar/output_relleno_fino/" 
    dir_output = "./output_Curvas_Interpolar/"
    
    print(dir_input)
    lista_dic = []
    for case in lista_input:
        print(case, "\n\n")
        input_directory = dir_input+case  # Replace with your input directory
        input_directory = "./input_Curvas_Interpolar/"
        
        output_directory = dir_output+case  # Replace with your output directory
        num_points = 10  # Number of interpolated points between each pair of rows

        lista_dic.append(main(input_directory, output_directory, num_points))

    print(lista_dic)