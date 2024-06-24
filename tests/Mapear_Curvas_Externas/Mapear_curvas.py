"""
Toma a todas las matrices que estan en .np y para cada valor del diccionario le asigna un valor mapeado
El valor mapeado indica en un string, entre que curvas esta el punto
El diccionario tiene el formato: valor -> 2 curvas
    "1.0" : (1.0 ,0.0 )
Rellenar con [c1 c2]

En la carpeta Input, estan las curvas rellenas, con las curvas exteriores.
No incluimos CL, ya que no tiene curvas exteriores
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


curvas_de_extrapolacion = {
     "Logg" : {
        "2.7" : (2.7 ,2.8 ), #Extrapolación
        "4.3" : (4.3 ,4.35), #Extrapolación
     },

     "Mbol" : {
        "-8.25": (-8.25,-7.5 ), #Extrapolación
        "-0.5" : (-0.5 ,-0.25), #Extrapolación
     },

     "Mv" : {
        "-6.25": (-6.25,-6.0 ), #Extrapolación
        "0.5"  : (0.5  ,0.75  ), #Extrapolación
     },

     "PHIo-Calientes" : {
        "0.665": (0.665 ,0.67), #Extrapolación
        "1.12" : (1.12 ,1.24 ), #Extrapolación  
     },

     "PHIo-Frias" : {
        "1.27" : (1.45 , 1.27), #Extrapolación
        "2.77" : (2.77, 2.65), #Extrapolación
     },

     "TE-Calientes" : {
        "6.0" :  (5.5, 6.0), #Extrapolación
        "25.0" : (23.0 ,25.0 ), #Extrapolación
     },

     "TE-Frias" : {
        "25.0" : (24.0 ,25.0 ), #Extrapolación
        "41.0" : (40.0 ,41.0), #Extrapolación
     },

     "Teff" : {
        "9250.0"  : (9500.0 , 9250.0 ), #Extrapolación
        "35000.0" : (37500.0 ,35000.0 ), #Extrapolación
     }
}

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
        "2.7" : (2.7 ,2.8 ), #Extrapolación
        "2.8" : (2.8 ,3.0 ),
        "3.0" : (3.0 ,3.2 ),
        "3.2" : (3.2 ,3.4 ),
        "3.4" : (3.4 ,3.6 ),
        "3.6" : (3.6 ,3.8 ),
        "3.8" : (3.8 ,4.0 ),
        "4.0" : (4.0 ,4.1 ), 
        "4.1" : (4.1 ,4.2 ),
        "4.2" : (4.2 ,4.3 ),
        "4.3" : (4.3 ,4.35), #Extrapolación
        "4.35": (None, None),
        "99999.0" :  (None , None ),       
        },

    "Mbol" : {
        "-8.25": (-8.0 ,-8.25), #Extrapolación
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
        "-0.5" : (-0.5 ,-0.25), #Extrapolación
        "-0.25": (None, None ), #Fuera del area de extrapolación
        "99999.0": (None , None ), #Fuera del area de extrapolación
        },

    "Mv" : {
        "-6.25": (-6.25,-6.0 ), #Extrapolación
        "-6.0" : (-5.0 ,-6.0 ),
        "-5.0" : (-4.0 ,-5.0 ),
        "-4.0" : (-3.0 ,-4.0 ),
        "-3.0" : (-2.0 ,-3.0 ),
        "-2.0" : (-1.0 ,-2.0 ),
        "-1.0" : (-0.5 ,-1.0 ),
        "-0.5" : (0.0  ,-0.5 ),
        "0.0"  : (0.5  ,0.0  ),
        "0.5"  : (0.5  ,0.75  ), #Extrapolación
        "0.75" : (None , None ), #Fuera del area de extrapolación
        "99999.0":(None , None ), #Fuera del area de extrapolación
    },

    "PHIo-Calientes" : {
        "0.665": (0.655 ,0.67), #Extrapolación
        "0.66" : (0.67 ,0.66 ),
        "0.67" : (0.68 ,0.67 ),
        "0.68" : (0.69 ,0.68 ),
        "0.69" : (0.7 ,0.69 ),
        "0.7"  : (0.72 ,0.7 ),
        "0.72" : (0.76 ,0.72 ),
        "0.76" : (0.8 ,0.76 ),
        "0.8"  : (0.86 ,0.8 ),
        "0.86" : (0.93 ,0.86 ),
        "0.93" : (1.05 ,0.93 ),
        "1.05" : (1.12 ,1.05 ),
        "1.12" : (1.12 ,1.24 ), #Extrapolación
        "1.24" : (None , None), #Fuera del area de extrapolación
        "99999.0" :  (None , None ), #Fuera del area de extrapolación
    },

    "PHIo-Frias" : {
        "1.16" : (None , None), #Fuera del area de extrapolación
        "1.27" : (1.27 , 1.16), #Extrapolación
        "1.45" : (1.45 , 1.27 ),
        "1.62" : (1.62 ,1.45 ),
        "1.77" : (1.77 ,1.62 ),
        "1.97" : (1.97 ,1.77 ),
        "2.14" : (2.14 ,1.97 ),
        "2.27" : (2.27 ,2.14 ),
        "2.4"  : (2.4 , 2.27 ),
        "2.65" : (2.65, 2.4 ),
        "2.77" : (2.77, 2.65), #Extrapolación
        "99999.0" :  (None , None ), #Fuera del area de extrapolación
        },
    
    "TE-Calientes" : {
        "5.5"  : (5.5, 6.0), #Extrapolación
        "6.0"  : (8.0 ,6.0 ), 
        "8.0"  : (10.0 ,8.0 ) ,
        "10.0" : (11.0 ,10.0 ),
        "11.0" : (12.0 ,11.0 ),
        "12.0" : (13.0 ,12.0 ),
        "13.0" : (15.0 ,13.0 ),
        "15.0" : (17.0 ,15.0 ),
        "17.0" : (19.0 ,17.0 ),
        "19.0" : (20.0 ,19.0 ),
        "20.0" : (22.0 ,20.0 ),
        "22.0" : (23.0 ,22.0 ),
        "23.0" : (23.0 ,25.0 ), #Extrapolación
        "25.0" : (None, None), #Fuerea del area de Extrapolación
        "99999.0" :  (None , None ), #Fuerea del area de Extrapolación
        },

    "TE-Frias" : {
        "24.0" : (None , None ),
        "25.0" : (24.0 ,25.0 ), #Extrapolación
        "27.0" : (27.0 ,25.0 ),
        "30.0" : (30.0 ,27.0 ),
        "32.0" : (32.0 ,30.0 ),
        "34.0" : (34.0 ,32.0 ),
        "36.0" : (36.0 ,34.0 ),
        "37.0" : (37.0 ,36.0 ),
        "38.0" : (38.0 ,37.0 ),
        "40.0" : (40.0 ,38.0 ),
        "41.0" : (41.0 ,40.0), #Extrapolación
        "99999.0" :  (None , None ),
        },
    
    "Teff" : {
        "9250.0"  : (9500.0 , 9250.0 ), #Extrapolación
        "9500.0"  : (9500.0 , 10000.0),
        "10000.0" : (10000.0 ,11000.0 ),
        "11000.0" : (11000.0 ,12500.0 ),
        "12500.0" : (12500.0 ,15000.0 ),
        "15000.0" : (15000.0 ,17500.0 ),
        "17500.0" : (17500.0 ,20000.0 ),
        "20000.0" : (20000.0 ,22500.0 ),
        "22500.0" : (22500.0 ,25000.0 ),
        "25000.0" : (25000.0 ,30000.0 ),
        "30000.0" : (30000.0 ,35000.0 ),
        "35000.0" : (37500.0 ,35000.0 ), #Extrapolación
        "37500.0" : (None , None),
        "99999.0" :  (None , None ),
        },
    
}

dir_input = "./input/"

dir_output = "./output/"

dir_output_txt = "./output_txt/"

#lee los archivo en un directorio
files = os.listdir(dir_input)

for file in files:
    print(file)
    #Read the file
    matriz = np.load(dir_input+file)
    print(matriz)
    # Map the file

    # For each value posible
    curve_name = file.split(".")[0]
    values = curves[curve_name]

    #Create the new matriz of type str
    
    new_matriz = np.zeros(matriz.shape, dtype = object)
    
    #para cada valor de la matriz, lo modifico por el valor mapeado
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]): 
            #Value contiene dos valores (a, b), donde a y b son las curvas que contienen el punto

            value = values[str(matriz[i][j])]
            new_value = str(value[0]) + " " + str(value[1])
            new_matriz[i][j] = new_value
   
    #save the new matriz
   
    file_txt = file.split(".")[0]+".txt"
    np.savetxt(dir_output_txt+file_txt, new_matriz, fmt='%-10s', delimiter='|')
    np.save(dir_output+file, new_matriz)        
            
    