import os

def interpolate_values(x1, y1, x2, y2, num_points):
    """
    Interpolate values between two points.
    """
    x_step = (x2 - x1) / (num_points + 1)
    y_step = (y2 - y1) / (num_points + 1)

    interpolated_values = [(x1 + i * x_step, y1 + i * y_step) for i in range(1, num_points + 1)]

    return interpolated_values

def interpolate_files(input_directory, output_directory, num_points):
    """
    Interpolate values between two points for all .dat files in the input directory.
    Save the interpolated files in the output directory.
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Get a list of all .dat files in the input directory
    input_files = [file for file in os.listdir(input_directory) if file.endswith(".dat")]

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

            for i in range(1, len(lines)):
                line = lines[i].split()
                
                x1, y1 = float(line[0]), float(line[1])

                if i < len(lines) - 1:
                    next_line = lines[i + 1].split()
                    x2, y2 = float(next_line[0]), float(next_line[1])

                    interpolated_values = interpolate_values(x1, y1, x2, y2, num_points)

                    for x, y in interpolated_values:
                        output_file.write(f"{x:.5f}     {y:.5f}\n")

                output_file.write(f"{x2:.5f}     {y2:.5f}\n")  # Write the last point

def main(input_directory, output_directory, num_points):
    interpolate_files(input_directory, output_directory, num_points)

if __name__ == "__main__":
    lista_input = ["CL/Calientes/", "CL/Frias/", "Logg/", "Mbol/", "PHIo/Frias/", "PHIo/Calientes/", "TE/Frias/", "TE/Calientes/", "Mv/", "Teff/"]
    
    dir_input = "./Curvas_Originales/Curvas/"
    dir_output = "./output_folder/" 
    
    print(dir_input)
    for case in lista_input:
        print(case)
        input_directory = dir_input+case  # Replace with your input directory
        
        output_directory = dir_output+case  # Replace with your output directory
        num_points = 2  # Number of interpolated points between each pair of rows

        main(input_directory, output_directory, num_points)
