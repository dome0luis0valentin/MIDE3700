import glob
import shutil

#Direcotirios de entrada
dir_input_a = "/home/valen/PPS/MIDE3700/tests/Agregar_area_extrapolar/output_relleno_fino_infeiores"
dir_input_b = "/home/valen/PPS/MIDE3700/tests/Agregar_area_extrapolar/output_relleno_fino_superiores"

dir_output = "/home/valen/PPS/MIDE3700/tests/Agregar_area_extrapolar/Curvas"

lista_input = ["Logg/", "Mbol/", "PHIo/Frias/", "PHIo/Calientes/", "TE/Frias/", "TE/Calientes/", "Mv/", "Teff/"]

for dir in lista_input:
    files_a = glob.glob(f'{dir_input_a}/{dir}/*.dat')
    files_b = glob.glob(f'{dir_input_b}/{dir}/*.dat')

    for file in files_a:
        #Copio el archivo en el directorio de salida
        shutil.copy(file, f"{dir_output}/{dir}")
    
    for file in files_b:
        shutil.copy(file, f"{dir_output}/{dir}")