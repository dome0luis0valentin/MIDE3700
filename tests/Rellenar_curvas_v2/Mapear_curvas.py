"""
Toma a todas las matrices que estan en .np y para cada valor del diccionario le asigna un valor mapeado
El valor mapeado indica en un string, entre que curvas esta el punto
El diccionario tiene el formato: valor -> 2 curvas
    "1.0" : (1.0 ,0.0 )
Rellenar con [c1 c2]
"""
import numpy as np
import os
import matplotlib.pyplot as plt

def plot_matrix_intensity( matrix):
        n = 850
        # Resize the matrix to nxn using interpolation
        resized_matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                row = int(i * (matrix.shape[0] / n))
                col = int(j * (matrix.shape[1] / n))
                resized_matrix[i, j] = matrix[row, col]

        # Plot the resized matrix as an image
        plt.imshow(resized_matrix, cmap='viridis', interpolation='nearest', origin='upper')
        plt.colorbar()
        plt.title('Matrix Intensity Plot')
        plt.show()

curves = {
    "CL-Calientes": {
        "1.0" : (1.0 ,2.0 ),
        "2.0" : (2.0 ,3.0 ),
        "3.0" : (3.0 ,4.0 ),
        "4.0" : (4.0 ,5.0 ),
        "5.0" : (5.0 ,6.0 ),
        "6.0" : (None, None ),
        "0.0" :  (0.0 ,1.0 ),
        "99999.0" :  (None , None ),
        },
    "CL-Frias": {
        "2.0" : (2.0 ,1.0 ),
        "3.0" : (3.0 ,2.0 ),
        "4.0" : (4.0 ,3.0 ),
        "5.0" : (5.0 ,4.0 ),
        "1.0" :  (None , None ),
        "99999.0" :  (None , None ),
        },
    "Landolt" : {},
    "Logg" : {
        "3.0" : (3.0 , 3.2 ),
        "3.2" : (3.2 ,3.0 ),
        "3.4000000000000004" : (3.4000000000000004 ,3.6000000000000005 ),
        "3.6000000000000005" : (3.6000000000000005 ,3.8000000000000007),
        "3.8000000000000007" : (3.8000000000000007 ,4.000000000000001),
        "4.000000000000001" : (4.000000000000001 ,4.1000000000000005 ),
        "4.1000000000000005" : (4.1000000000000005 ,4.2 ),
        "4.2" : (4.2 ,4.3 ),
        "4.3" : (None, None ),
        "2.8" :  (2.8 , 3.0),
        "99999.0" :  (None , None ),       
        },
    "Mbol" : {
        "-8.0" : (-7.5 ,-8.0 ),
        "-7.5" : (-7.0 ,-7.5 ),
        "-7.0" : (-6.5 ,-7.0 ),
        "-6.5" : (-6.0 ,-6.5 ),
        "-6.0" : (-5.5 ,-6.0 ),
        "-5.5" : (-5.0 ,-5.5 ),
        "-5.0" : (-4.5 ,-5.0 ),
        "-4.5" : (-4.0 ,-4.5 ),
        "-4.0" : (-3.5 ,-4.0 ),
        "-3.5" : (-3.0 ,-3.5 ),
        "-3.0" : (-2.5 ,-3.0 ),
        "-2.5" : (-2.0 ,-2.5 ),
        "-2.0" : (-1.5 ,-2.0 ),
        "-1.5" : (-1.0 ,-1.5 ),
        "-1.0" : (-0.5 ,-1.0 ),
        "-0.5" :  (None , None ),
        "99999.0" :  (None , None ),
        },
    "Mv" : {
        "-6.0" : (-5.0 ,-6.0 ),
        "-5.0" : (-4.0 ,-5.0 ),
        "-4.0" : (-3.0 ,-4.0 ),
        "-3.0" : (-2.0 ,-3.0 ),
        "-2.0" : (-1.0 ,-2.0 ),
        "-1.0" : (-0.5 ,-1.0 ),
        "-0.5" : (0.0  ,-0.5 ),
        "0.0" :  (0.5  ,0.0  ),
        "0.5" :  (None , None ),
        "99999.0":(None , None ),
    },
    "PHIo-Calientes" : {
        "0.66" : (0.67 ,0.66 ),
        "0.67" : (0.68 ,0.67 ),
        "0.68" : (0.69 ,0.68 ),
        "0.69" : (0.7 ,0.69 ),
        "0.7" : (0.72 ,0.7 ),
        "0.72" : (0.76 ,0.72 ),
        "0.76" : (0.8 ,0.76 ),
        "0.8" : (0.86 ,0.8 ),
        "0.86" : (0.93 ,0.86 ),
        "0.93" : (1.05 ,0.93 ),
        "1.05" : (1.12 ,1.05 ),
        "1.12" : (1.27 ,1.12 ),
        "1.27" :  (None , None ),
        "99999.0" :  (None , None ),
        },
    "PHIo-Frias" : {
        "1.62" : (1.62 ,1.45 ),
        "1.77" : (1.77 ,1.62 ),
        "1.97" : (1.97 ,1.77 ),
        "2.14" : (2.14 ,1.97 ),
        "2.27" : (2.27 ,2.14 ),
        "2.4" : (2.4 ,2.27 ),
        "2.65" : (2.65 ,2.4 ),
        "1.45" :  (1.45 , 1.27 ),
        "1.27" :  (None , None ),
        "99999.0" :  (None , None ),
        },
    "TE-Calientes" : {
        "8.0" : (8.0 ,6.0 ),
        "10.0" : (10.0 ,8.0 ),
        "11.0" : (11.0 ,10.0 ),
        "12.0" : (12.0 ,11.0 ),
        "13.0" : (13.0 ,12.0 ),
        "15.0" : (15.0 ,13.0 ),
        "17.0" : (17.0 ,15.0 ),
        "19.0" : (19.0 ,17.0 ),
        "20.0" : (20.0 ,19.0 ),
        "22.0" : (22.0 ,20.0 ),
        "23.0" : (23.0 ,22.0 ),
        "25.0" : (25.0 ,23.0 ),
        "6.0" :  (None , None ),
        "99999.0" :  (None , None ),
        },
    "TE-Frias" : {
        "27.0" : (27.0 ,25.0 ),
        "30.0" : (30.0 ,27.0 ),
        "32.0" : (32.0 ,30.0 ),
        "34.0" : (34.0 ,32.0 ),
        "36.0" : (36.0 ,34.0 ),
        "37.0" : (37.0 ,36.0 ),
        "38.0" : (38.0 ,37.0 ),
        "40.0" : (40.0 ,38.0 ),
        "25.0" :  (None , None ),
        "99999.0" :  (None , None ),
        },
    "Teff" : {
        "10000.0" : (10000.0 ,9500.0 ),
        "11000.0" : (11000.0 ,10000.0 ),
        "12500.0" : (12500.0 ,11000.0 ),
        "15000.0" : (15000.0 ,12500.0 ),
        "17500.0" : (17500.0 ,15000.0 ),
        "20000.0" : (20000.0 ,17500.0 ),
        "22500.0" : (22500.0 ,20000.0 ),
        "25000.0" : (25000.0 ,22500.0 ),
        "30000.0" : (30000.0 ,25000.0 ),
        "35000.0" : (35000.0 ,30000.0 ),
        "9500.0" :  (None , None ),
        "99999.0" :  (None , None ),
        },
    
}

dir_input = "../Curvas_Numpy/"

dir_output = "/home/valen/PPS/MIDE3700/tests/Rellenar_curvas_v2/output_nuevas_curvas_np/"

#lee los archivo en un directorio
files = os.listdir(dir_input)

for file in files:
    print(file)
    #Read the file
    matriz = np.load(dir_input+file)
    # Map the file

    # For each value posible
    curve_name = file.split(".")[0]
    values = curves[curve_name]

    #Create the new matriz of type str
    
    new_matriz = np.zeros(matriz.shape, dtype = object)
    #para cada valor de la matriz, lo modifico por el valor mapeado
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]): 
            value = values[str(matriz[i][j])]
            new_value = str(value[0]) + " " + str(value[1])
            new_matriz[i][j] = new_value
    
    #save the new matriz
    if file.split(".")[0] == "Teff":
        file_txt = file.split(".")[0]+".txt"
        # np.savetxt(dir_output+file_txt, new_matriz, fmt='%-15s', delimiter='|', newline='\n')
        np.save(dir_output+file, new_matriz)

    else:
        file_txt = file.split(".")[0]+".txt"
        # np.savetxt(dir_output+file_txt, new_matriz, fmt='%-10s', delimiter='|')
        np.save(dir_output+file, new_matriz)        
            
    