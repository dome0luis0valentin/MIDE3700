import os
import numpy as np

dir_curvas = "/home/valen/PPS/MIDE3700/tests/Superponer_matrices/input_curvas/"
dir_matrices = "/home/valen/PPS/MIDE3700/tests/Superponer_matrices/input_matrices_rellenas/"

dir_output = "/home/valen/PPS/MIDE3700/tests/Superponer_matrices/output/"

dir_output_text = "/home/valen/PPS/MIDE3700/tests/Superponer_matrices/output_text/"
file_curvas = sorted(os.listdir(dir_curvas))
file_matrices = sorted(os.listdir(dir_matrices))

#Crea una matriz con dimensiones desconocidas
nueva_matriz = np.zeros((1,1))

for curva, matriz in zip(file_curvas, file_matrices):
    nombre = curva.split("/")[-1]

    curva_np = np.load(dir_curvas+curva, allow_pickle=True)

    matriz_np = np.load(dir_matrices+matriz, allow_pickle=True)

    print(f"Dimensiones de las matrices: {curva_np.shape}, matriz: {matriz_np.shape}")
    

    for i in range(curva_np.shape[0]):
        for j in range(curva_np.shape[1]): 
            value = curva_np[i][j]
            if value != 99999.0:
                value_float64 = np.float64(value)
                matriz_np[i][j] = value_float64

    np.save(dir_output+nombre, matriz_np)
    np.savetxt(dir_output_text+nombre+".txt", matriz_np, fmt='%-10s', delimiter='|')
 
    print(matriz, curva)