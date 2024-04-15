#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
import numpy as np
import math
import Algebra
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

from Funciones_auxiliares import point_in_triangle, calcular_min_distance, distancia_euclidea, distancia_euclidea_v2
from tests.generar_matriz_desde_texto import cargar_matriz_desde_archivo, matrices_son_iguales

class Curvas:
    # Atributos de la clase
    archivo_in= ""    # Nombre del archivo que tiene la lista de curvas
    cte_curvas= []    # Guarda el valor constante de cada curva
    x0= float()       # Inicio del eje x
    xn= float()       # Fin del eje x
    y0= float()       # Inicio del eje y
    yn= float()       # Fin del eje y
    kx= int()         # Escaleo del eje x
    ky= int()         # Escaleo del eje y
    nc= int()         # Cantidad de curvas de nivel
    matriz= [[],[]]   # Matriz que guarda las curvas de nivel
    #---------------------------------------------------------------------------
    def __init__(self, magnitud):
        self.archivo_in= "Input/Curva" + magnitud + ".in"
        self.cte_curvas= []
        self.matriz= [[],[]]
        self.Cargo_Curva(magnitud)
        return
    #---------------------------------------------------------------------------
    
    def cargo_curvas_rellenas(self, magnitud):

        print("Cargo curvas de ", magnitud," \ Load ", magnitud, " curves\n")

        if magnitud == "Teff":

            self.nc= 11

            self.cte_curvas.append( 9500. )
            self.cte_curvas.append( 10000. )
            self.cte_curvas.append( 11000. )
            self.cte_curvas.append( 12500. )
            self.cte_curvas.append( 15000. )
            self.cte_curvas.append( 17500. )
            self.cte_curvas.append( 20000. )
            self.cte_curvas.append( 22500. )
            self.cte_curvas.append( 25000. )
            self.cte_curvas.append( 30000. )
            self.cte_curvas.append( 35000. )

            self.x0= 0.
            self.xn= 0.55
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "TE_c":

            self.nc= 13

            # A cada tipo espectral le asignamos le asignamos un numero entero:
            # O0 => 0
            # B0 => 10
            # A0 => 20

            self.cte_curvas.append(  6. )# => tipo espectral O6
            self.cte_curvas.append(  8. )# => tipo espectral O8
            self.cte_curvas.append( 10. )# => tipo espectral B0
            self.cte_curvas.append( 11. )# => tipo espectral B1
            self.cte_curvas.append( 12. )# => tipo espectral B2
            self.cte_curvas.append( 13. )# => tipo espectral B3
            self.cte_curvas.append( 15. )# => tipo espectral B5
            self.cte_curvas.append( 17. )# => tipo espectral B7
            self.cte_curvas.append( 19. )# => tipo espectral B9
            self.cte_curvas.append( 20. )# => tipo espectral A0
            self.cte_curvas.append( 22. )# => tipo espectral A2
            self.cte_curvas.append( 23. )# => tipo espectral A3
            self.cte_curvas.append( 25. )# => tipo espectral A5

            self.x0= 0.
            self.xn= 0.70
            self.y0= -5.
            self.yn= 80.
            self.kx= 10000
            self.ky= 10

        elif magnitud == "TE_f":

            self.nc= 9

            # A cada tipo espectral le asignamos le asignamos un numero entero:
            # A0 => 20
            # F0 => 30
            # G0 => 40

            self.cte_curvas.append( 25. )# => tipo espectral A5
            
            #MODIFICO WARNING AVISO ACA YAEL
            # self.cte_curvas.append( 37. )# => tipo espectral A7 
            self.cte_curvas.append( 27. )# => tipo espectral A7
            self.cte_curvas.append( 30. )# => tipo espectral F0
            self.cte_curvas.append( 32. )# => tipo espectral F2
            self.cte_curvas.append( 34. )# => tipo espectral F4
            self.cte_curvas.append( 36. )# => tipo espectral F6
            self.cte_curvas.append( 37. )# => tipo espectral F7
            self.cte_curvas.append( 38. )# => tipo espectral F8
            self.cte_curvas.append( 40. )# => tipo espectral G0

            self.x0= 0.
            self.xn= 0.70
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "CL_c":

            self.nc= 7

            # A cada clase de luminosidad le asignamos le asignamos un numero entero:
            # Ia => 0
            # Ib => 1
            # II => 2
            # III => 3
            # IV => 4
            # V => 5
            # VI => 6

            self.cte_curvas.append( 0. )
            self.cte_curvas.append( 1. )
            self.cte_curvas.append( 2. )
            self.cte_curvas.append( 3. )
            self.cte_curvas.append( 4. )
            self.cte_curvas.append( 5. )
            self.cte_curvas.append( 6. )

            self.x0= 0.
            self.xn= 0.70
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "CL_f":

            self.nc= 5

            # A cada clase de luminosidad le asignamos le asignamos un numero entero:
            # Ia => 0
            # Ib => 1
            # II => 2
            # III => 3
            # IV => 4
            # V => 5
            # VI => 6

            self.cte_curvas.append( 1. )
            self.cte_curvas.append( 2. )
            self.cte_curvas.append( 3. )
            self.cte_curvas.append( 4. )
            self.cte_curvas.append( 5. )

            self.x0= 0.
            self.xn= 0.70
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "Logg":

            self.nc= 10

            self.cte_curvas.append( 2.8 )
            for i in range( 1, 7):
                self.cte_curvas.append( self.cte_curvas[i-1] + 0.2 )
            for i in range( 7, self.nc):
                self.cte_curvas.append( self.cte_curvas[i-1] + 0.1 )

            self.x0= 0.
            self.xn= 0.7
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "Mv":

            self.nc= 9

            for i in range( -6, 0):
                self.cte_curvas.append( float(i) )
                
            self.cte_curvas.append( -0.5 )
            self.cte_curvas.append( 0.0 )
            self.cte_curvas.append( 0.5 )

            self.x0= 0.
            self.xn= 0.7
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "Mbol":

            self.nc= 16

            self.cte_curvas.append( -8.0 )
            for i in range( 1, self.nc):
                self.cte_curvas.append( self.cte_curvas[i-1] + 0.5 )

            self.x0= 0.
            self.xn= 0.7
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10
        elif magnitud == "PHIo_c":

            self.nc= 13

            self.cte_curvas.append( 0.66 )
            self.cte_curvas.append( 0.67 )
            self.cte_curvas.append( 0.68 )
            self.cte_curvas.append( 0.69 )
            self.cte_curvas.append( 0.70 )
            self.cte_curvas.append( 0.72 )
            self.cte_curvas.append( 0.76 )
            self.cte_curvas.append( 0.80 )
            self.cte_curvas.append( 0.86 )
            self.cte_curvas.append( 0.93 )
            self.cte_curvas.append( 1.05 )
            self.cte_curvas.append( 1.12 )
            self.cte_curvas.append( 1.27 )

            self.x0= 0.
            self.xn= 0.70
            self.y0= -8.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "PHIo_f":

            self.nc= 9

            self.cte_curvas.append( 1.27 )
            self.cte_curvas.append( 1.45 )
            self.cte_curvas.append( 1.62 )
            self.cte_curvas.append( 1.77 )
            self.cte_curvas.append( 1.97 )
            self.cte_curvas.append( 2.14 )
            self.cte_curvas.append( 2.27 )
            self.cte_curvas.append( 2.40 )
            self.cte_curvas.append( 2.65 )

            self.x0= 0.
            self.xn= 0.70
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        curvas_in= self.Leo_Archivo()
        self.Matriz_Curvas(curvas_in)
        return
    #---------------------------------------------------------------------------
    
    def Cargo_Curva(self, magnitud):

        print("Cargo curvas de ", magnitud," \ Load ", magnitud, " curves\n")

        if magnitud == "Teff":

            self.nc= 11

            self.cte_curvas.append( 9500. )
            self.cte_curvas.append( 10000. )
            self.cte_curvas.append( 11000. )
            self.cte_curvas.append( 12500. )
            self.cte_curvas.append( 15000. )
            self.cte_curvas.append( 17500. )
            self.cte_curvas.append( 20000. )
            self.cte_curvas.append( 22500. )
            self.cte_curvas.append( 25000. )
            self.cte_curvas.append( 30000. )
            self.cte_curvas.append( 35000. )

            self.x0= 0.
            self.xn= 0.55
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "TE_c":

            self.nc= 12

            # A cada tipo espectral le asignamos le asignamos un numero entero:
            # O0 => 0
            # B0 => 10
            # A0 => 20

            self.cte_curvas.append(  6. )# => tipo espectral O6
            self.cte_curvas.append(  8. )# => tipo espectral O8
            self.cte_curvas.append( 10. )# => tipo espectral B0
            self.cte_curvas.append( 11. )# => tipo espectral B1
            self.cte_curvas.append( 12. )# => tipo espectral B2
            self.cte_curvas.append( 13. )# => tipo espectral B3
            self.cte_curvas.append( 15. )# => tipo espectral B5
            self.cte_curvas.append( 17. )# => tipo espectral B7
            self.cte_curvas.append( 19. )# => tipo espectral B9
            self.cte_curvas.append( 20. )# => tipo espectral A0
            self.cte_curvas.append( 22. )# => tipo espectral A2
            self.cte_curvas.append( 23. )# => tipo espectral A3
            # self.cte_curvas.append( 25. )# => tipo espectral A5

            self.x0= 0.
            self.xn= 0.70
            self.y0= -5.
            self.yn= 80.
            # self.kx= 10000
            self.kx= 100
            self.ky= 10

        elif magnitud == "TE_f":

            self.nc= 9

            # A cada tipo espectral le asignamos le asignamos un numero entero:
            # A0 => 20
            # F0 => 30
            # G0 => 40

            self.cte_curvas.append( 25. )# => tipo espectral A5
            
            #MODIFICO WARNING AVISO ACA YAEL
            # self.cte_curvas.append( 37. )# => tipo espectral A7 
            self.cte_curvas.append( 27. )# => tipo espectral A7
            self.cte_curvas.append( 30. )# => tipo espectral F0
            self.cte_curvas.append( 32. )# => tipo espectral F2
            self.cte_curvas.append( 34. )# => tipo espectral F4
            self.cte_curvas.append( 36. )# => tipo espectral F6
            self.cte_curvas.append( 37. )# => tipo espectral F7
            self.cte_curvas.append( 38. )# => tipo espectral F8
            self.cte_curvas.append( 40. )# => tipo espectral G0

            self.x0= 0.
            self.xn= 0.70
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "CL_c":

            self.nc= 7

            # A cada clase de luminosidad le asignamos le asignamos un numero entero:
            # Ia => 0
            # Ib => 1
            # II => 2
            # III => 3
            # IV => 4
            # V => 5
            # VI => 6

            self.cte_curvas.append( 0. )
            self.cte_curvas.append( 1. )
            self.cte_curvas.append( 2. )
            self.cte_curvas.append( 3. )
            self.cte_curvas.append( 4. )
            self.cte_curvas.append( 5. )
            self.cte_curvas.append( 6. )

            self.x0= 0.
            self.xn= 0.70
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "CL_f":

            self.nc= 5

            # A cada clase de luminosidad le asignamos le asignamos un numero entero:
            # Ia => 0
            # Ib => 1
            # II => 2
            # III => 3
            # IV => 4
            # V => 5
            # VI => 6

            self.cte_curvas.append( 1. )
            self.cte_curvas.append( 2. )
            self.cte_curvas.append( 3. )
            self.cte_curvas.append( 4. )
            self.cte_curvas.append( 5. )

            self.x0= 0.
            self.xn= 0.70
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "Logg":

            self.nc= 10

            self.cte_curvas.append( 2.8 )
            for i in range( 1, 7):
                self.cte_curvas.append( self.cte_curvas[i-1] + 0.2 )
            for i in range( 7, self.nc):
                self.cte_curvas.append( self.cte_curvas[i-1] + 0.1 )

            self.x0= 0.
            self.xn= 0.7
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "Mv":

            self.nc= 9

            for i in range( -6, 0):
                self.cte_curvas.append( float(i) )
                
            self.cte_curvas.append( -0.5 )
            self.cte_curvas.append( 0.0 )
            self.cte_curvas.append( 0.5 )

            self.x0= 0.
            self.xn= 0.7
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "Mbol":

            self.nc= 16

            self.cte_curvas.append( -8.0 )
            for i in range( 1, self.nc):
                self.cte_curvas.append( self.cte_curvas[i-1] + 0.5 )

            self.x0= 0.
            self.xn= 0.7
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10
        elif magnitud == "PHIo_c":

            self.nc= 13

            self.cte_curvas.append( 0.66 )
            self.cte_curvas.append( 0.67 )
            self.cte_curvas.append( 0.68 )
            self.cte_curvas.append( 0.69 )
            self.cte_curvas.append( 0.70 )
            self.cte_curvas.append( 0.72 )
            self.cte_curvas.append( 0.76 )
            self.cte_curvas.append( 0.80 )
            self.cte_curvas.append( 0.86 )
            self.cte_curvas.append( 0.93 )
            self.cte_curvas.append( 1.05 )
            self.cte_curvas.append( 1.12 )
            self.cte_curvas.append( 1.27 )

            self.x0= 0.
            self.xn= 0.70
            self.y0= -8.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        elif magnitud == "PHIo_f":

            self.nc= 9

            self.cte_curvas.append( 1.27 )
            self.cte_curvas.append( 1.45 )
            self.cte_curvas.append( 1.62 )
            self.cte_curvas.append( 1.77 )
            self.cte_curvas.append( 1.97 )
            self.cte_curvas.append( 2.14 )
            self.cte_curvas.append( 2.27 )
            self.cte_curvas.append( 2.40 )
            self.cte_curvas.append( 2.65 )

            self.x0= 0.
            self.xn= 0.70
            self.y0= -5.
            self.yn= 80.
            self.kx= 100
            self.ky= 10

        curvas_in= self.Leo_Archivo()
        m1 = self.Matriz_Curvas(curvas_in)
        # self.Matriz_Curvas_Rellenas(curvas_in)
        # print("Matrices iguales: ", matrices_son_iguales(m1, m2))
        return
    #---------------------------------------------------------------------------
    def Leo_Archivo(self):
        with open(self.archivo_in, 'r') as f_curva:
            return [linea.split()[0] for linea in f_curva if linea.strip()]
        
    """
    def Leo_Archivo(self):
        f_curva= open(self.archivo_in, 'r') # Abro el archivo de lectura
        linea= f_curva.readline()
        curvas_in= []

        # Leemeos el archivo
        while linea != "": # Lee linea por linea hasta el final del archivo
            # Como las columnas estan separadas por espacios guardamos las columnas
            # en una lista
            columna= linea.split("  ")
            n= len( str(columna[0]) )
            col= str( columna[0] )[0:n-1]
            curvas_in.append( col )# Primera columna del archivo
            linea= f_curva.readline()# leemos la siguiente linea del archivo

        f_curva.close()
        return curvas_in
    """
    
    def save_matrix_to_file(self, matrix, filename):
        """
        Save a matrix to a file.

        Parameters:
        - matrix: 2D NumPy array or list of lists representing the matrix.
        - filename: String, the name of the file to save the matrix.

        Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> save_matrix_to_file(matrix, 'matrix.txt')
        """
        # Convert the matrix to a NumPy array if it's not already
        matrix_array = np.array(matrix)

        # Get the maximum value length in the matrix
        max_length = len(str(np.max(matrix_array)))
        
        # Format each value to occupy the same space
        formatted_matrix = [[f"{value:>{max_length}}" for value in row] for row in matrix_array]

        # Save the formatted matrix to the specified file
        np.savetxt(filename, formatted_matrix, fmt='%s', delimiter=', ')

    def plot_matrix_intensity(self, matrix):
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

    def mostrar_matriz(self, matriz, titulo):
        # Convert the matrix to a numpy array
        matriz_np = np.array(matriz)

        # Create a figure and axis
        # fig, ax = plt.subplots()

        # Display the matrix using imshow with intensity-based color mapping
        ax.imshow(matriz_np, cmap='viridis', vmin=np.min(matriz_np), vmax=np.max(matriz_np))

        # Set the title
        ax.set_title(titulo)
        
        # Set the aspect ratio to 'equal'
        ax.set_aspect('equal')

        # Show the plot
        plt.show()

    def colorear_horizontal(self, matriz):
        ancho_matriz = matriz.shape[1]-1
        
        vacio = 99999.0
        valor_actual = vacio
        
        for fila in matriz:
            index = 0
            
            #busco el primer punto de la curva
            while (fila[index] == vacio and index < ancho_matriz):
                index += 1
                    
            #relleno con ese valor hasta la próxima curva
            valor_actual = fila[index]
                        
            #no se termine la matriz
            while (index < ancho_matriz):
                
                #no llegue a otra curva
                while ( (fila[index] == vacio or fila[index] == valor_actual )and index < ancho_matriz):
                    fila[index] = valor_actual
                    index += 1
                    
                #cambio al nuevo valor de la curva
                valor_actual = fila[index]
    
    def colorear_horizontal_inverso(self, matriz):
        ancho_matriz = matriz.shape[1]-1
            
        vacio = 99999.0
        valor_actual = vacio
            
        for fila in matriz:
            index = ancho_matriz
                
            #busco el primer punto de la curva
            while (fila[index] == vacio and index > 0):
                index -= 1
                        
                #relleno con ese valor hasta la próxima curva
            valor_actual = fila[index]
                            
                #no se termine la matriz
            while (index > 0):
                    
                    #no llegue a otra curva
                while ( (fila[index] == vacio or fila[index] == valor_actual )and index > 0):
                    fila[index] = valor_actual
                    index -= 1
                        
                    #cambio al nuevo valor de la curva
                valor_actual = fila[index]

    def colorear_vertical(self, matriz):

        ancho_matriz = matriz.shape[1]
        alto_matriz = len(matriz)-1
        
        vacio = 99999.0
        valor_actual = vacio
        
        for col in range(ancho_matriz):
            index = 0
            
            # busco el primer punto de la curva
            while (matriz[index][col] == vacio and index < alto_matriz):
                index += 1
                    
            # relleno con ese valor hasta la próxima curva
            valor_actual = matriz[index][col]
            
            # no se termine la matriz
            while (index < alto_matriz):
                
                # no llegue a otra curva
                while ((matriz[index][col] == vacio or matriz[index][col] == valor_actual) and index < alto_matriz):
                    matriz[index][col] = valor_actual
                    index += 1
                    
                # cambio al nuevo valor de la curva
                if index < alto_matriz:
                    valor_actual = matriz[index][col]
    
    def colorear_matriz(self, matriz, titulo):
        """ """
        print(titulo)
        if (titulo == "PHIo-Calientes"):
            np.savetxt("Phio-Calientes.txt", matriz, fmt='%s', delimiter=', ')

        if (titulo == "Logg" or titulo.startswith("CL-C") or (titulo == "Mbol") or (titulo.startswith("TE-C")) ):        
            self.colorear_horizontal(matriz)      
        else:
            if (titulo.startswith("CL-F")):
                self.colorear_horizontal_inverso(matriz)
            else:
                self.colorear_vertical(matriz)
            # print(f" \n\n {fila} \n\n")
        
        self.save_matrix_to_file(matriz, "./tests/Curvas_en_text/"+titulo + ".txt")    

        with open("./tests/Curvas_Numpy/"+titulo+".npy", 'wb') as f:
            np.save(f, matriz) 

        # self.mostrar_matriz(matriz, titulo)
    
    def nombrar_archivo(self, curvas_in):
        """
        Dada la ruta de una archivo le devuelve el nombre
        si es que tiene una carpeta en el medio el nombre sera  
        la 2da carpeta.

        Args:
            curvas_in (list): lista de directorios

        Returns:
            sting : nombre del archivo
            
        """
        titulo = ""
        parseo_ruta = curvas_in[0].split("/")
        if len(parseo_ruta) == 3:
            titulo = parseo_ruta[1]
        else:
            titulo = parseo_ruta[1]+"-"+parseo_ruta[2]     
            
        return titulo
        
    #---------------------------------------------------------------------------
    def Matriz_Curvas_Rellenas(self, curvas_in):
        """
        Version: 2.0
        Carga la matriz de curvas desde un archivo de texto
        """
        
        titulo = self.nombrar_archivo(curvas_in)
        # matriz = cargar_matriz_desde_archivo("./tests/Curvas_en_text/"+titulo + ".txt")
        self.matriz = np.load("./tests/Curvas_Numpy/"+titulo+".npy")
    
        return self.matriz
    
    def Matriz_Curvas(self, curvas_in):
        # Parametrizamos el eje x
        # i1 : primer punto del eje x
        # i2 : ultimo punto del eje x

        titulo = self.nombrar_archivo(curvas_in)

        if self.x0 >= 0.:
            i1= Algebra.Redondeo_int_mas_cerca( self.x0 * float(self.kx) )
            i2= Algebra.Redondeo_int_mas_cerca( self.xn * float(self.kx) )
        else:
            i1= 0
            i2= Algebra.Redondeo_int_mas_cerca( (self.xn + abs(self.x0)) * float(self.kx) )

        # Parametrizamos el eje y

        if self.y0 >= 0.:
            j1= Algebra.Redondeo_int_mas_cerca( self.y0 * float(self.ky) )
            j2= Algebra.Redondeo_int_mas_cerca( self.yn * float(self.ky) )
        else:
            j1= 0
            j2= Algebra.Redondeo_int_mas_cerca( (self.yn + abs(self.y0)) * float(self.ky) )

# Inicializo la matriz con numeros exageradamente grandes
        """
        self.matriz= np.zeros( [i2+1,j2+1] , float )
        for i in range(i1,i2):
            for j in range(j1,j2):
                self.matriz[i][j]= 99999.
        """
       
        # Crear una matriz llena de 99999.0
        
        # Creo una matriz de solo flotantes
        self.matriz = np.full((i2+1, j2+1), 99999.0, dtype=float)

        # Leo todos los archivos de las curvas
        
        
        #Agrego cada curva a la matriz
        for i in range(self.nc):
            with open(curvas_in[i], 'r') as f_curva:
                
                next(f_curva)  # Saltar la primera línea
                
                for linea in f_curva:

                    xy = [float(j) for j in linea.split() if j]
                    if not self.x0 <= xy[0] <= self.xn or not self.y0 <= xy[1] <= self.yn:
                        continue

                    ii = Algebra.Redondeo_int_mas_cerca((xy[0] + abs(self.x0)) * float(self.kx)) if self.x0 < 0. else Algebra.Redondeo_int_mas_cerca(xy[0] * float(self.kx))
                    jj = Algebra.Redondeo_int_mas_cerca((xy[1] + abs(self.y0)) * float(self.ky)) if self.y0 < 0. else Algebra.Redondeo_int_mas_cerca(xy[1] * float(self.ky))

                    # En esta posición de la matriz almaceno el valor que tiene la curva, que es un valor constante
                    #Actualizo la celda
                    if (self.matriz[ii][jj] == 99999.):
                        self.matriz[ii][jj] = self.cte_curvas[i]

        np.save("/home/valen/PPS/MIDE3700/tests/Rellenar_curvas_v2/input_matrices_con_curvas/"+titulo, self.matriz )
        np.savetxt("/home/valen/PPS/MIDE3700/tests/Rellenar_curvas_v2/input_m_in_text/"+titulo+".txt", self.matriz, fmt='%s', delimiter=' | ')
        self.colorear_matriz(self.matriz, titulo)

        # iguales = matrices_son_iguales(self.matriz, cargar_matriz_desde_archivo("./tests/Curvas_en_text/"+titulo + ".txt"))   
        # print(f" {titulo} es igual a la matriz cargada? {iguales} \n\n")

        #obsoleto?
        """
        for i in range(self.nc):
            f_curva= open(curvas_in[i], 'r') # Abro el archivo de lectura
            linea= f_curva.readline()
            linea= f_curva.readline()
            xy= [0., 0.]
            while linea != "":
                columna= linea.split(" ")
                jj= 0
                for j in columna:
                    if j != "":
                        xy[jj]= float( j )
                        jj= 1

                if self.x0 <= xy[0] and xy[0] <= self.xn and self.y0 <= xy[1] and xy[1] <= self.yn:
                    if self.x0 >= 0.:
                        ii= Algebra.Redondeo_int_mas_cerca( xy[0] * float(self.kx) )
                    else:
                        ii= Algebra.Redondeo_int_mas_cerca( (xy[0] + abs(self.x0)) * float(self.kx) )

                    if self.y0 >= 0.:
                        jj= Algebra.Redondeo_int_mas_cerca( xy[1] * float(self.ky) )
                    else:
                        jj= Algebra.Redondeo_int_mas_cerca( (xy[1] + abs(self.y0)) * float(self.ky) )

                    self.matriz[ii][jj]= self.cte_curvas[i]

                linea= f_curva.readline()# leemos la siguiente linea del archivo
            f_curva.close()
        
        """
        
        return self.matriz
    #---------------------------------------------------------------------------
    
    
    def Parametrizar(self, x, y):
        """     
        xx e yy son redimencionados para acceder a la matriz
        devuelve en i1, i2 las dimensiones de la matriz en el eje x
        devuelve en j1, j2 las dimensiones de la matriz en el eje y
        """
        
        if self.x0 >= 0.:
            i1= Algebra.Redondeo_int_mas_cerca( self.x0 * float(self.kx) )
            i2= Algebra.Redondeo_int_mas_cerca( self.xn * float(self.kx) )
            xx= x * float(self.kx)
        else:
            i1= 0
            i2= Algebra.Redondeo_int_mas_cerca( (self.xn + abs(self.x0)) * float(self.kx) )
            xx= (x + abs(self.x0)) * float(self.kx)

        # Parametrizamos el eje y y la coordenada y del punto

        if self.y0 >= 0.:
            j1= Algebra.Redondeo_int_mas_cerca( self.y0 * float(self.ky) )
            j2= Algebra.Redondeo_int_mas_cerca( self.yn * float(self.ky) )
            yy= y * float(self.ky)
        else:
            j1= 0
            j2= Algebra.Redondeo_int_mas_cerca( (self.yn + abs(self.y0)) * float(self.ky) )
            yy= (y + abs(self.y0)) * float(self.ky)
            
        return i1, i2, xx, j1, j2, yy
    
    def leer_curva(self, file):
        """
        Dada la dirección de un archivo, lo lee y devuelve sus filas en una lista de tuplas
        """
        with open(file, 'r') as f_curva:
                
            next(f_curva)  # Saltar la primera línea

            lista_puntos = []

            for linea in f_curva:
                xy = tuple(map(float, linea.split()))
                lista_puntos.append((xy))

        return lista_puntos

    def graficar_curvas(self, curvas_in, curvas, axes):
        """
        Dibuja 2 curvas en un plano, para representar graficamente el problema
        """

        index_files = []

        for constante in curvas:
            constantes = self.cte_curvas
            for i in range(len(constantes)):
                if ( constantes[i] == constante ):
                    index_files.append(curvas_in[i].replace("Curvas/", "/home/valen/PPS/MIDE3700/tests/Suavisar/Output_Suavisar/"))
                    break

        x_v, y_v =  self.dibujar_dos_curvas(index_files, axes)

        return x_v, y_v
    
    def dibujar_dos_curvas(self, file_list, axes):
        """
        Grafica la curva que se pasa como parametro
        """

        x_values = []
        y_values = []
        
        list_curves = []
        
        # Iterate over the files
        valores = []
        for file_path in file_list:
            # Open the file and read the coordinates
            with open(file_path, 'r') as f:
                
                for line in f:
                    if line.startswith("#"):
                        continue
                    else:
                        valores = list(map(float, line.strip().split()))
                       
                        x, y = valores[0], valores[1]
                        x_values.append(x)
                        y_values.append(y)
                        
            # Create a scatter plot
        
        plt.scatter(x_values, y_values, color='blue', marker='.')  

        return x_values, y_values
    
    def get_puntos_curva_completa(self, curvas_in, curva):
        """
        Dada una constante, devuelve una lista de pares x, y con los puntos que representan la curva 
        """
        lista_puntos = []
        index_file = -1

        constantes = self.cte_curvas
        for i in range(len(constantes)):
            if ( constantes[i] == curva ):
                index_file = i
                break
        
        lista_puntos = self.leer_curva(curvas_in[index_file])
        
        return lista_puntos
    
    def get_puntos_curva(self,curvas_in, curva):
        """
        Dada una constante, devuelve una lista de pares x, y con los puntos que representan una
        aproximación de la curva.
        """

        lista_puntos = []
        index_file = -1

        constantes = self.cte_curvas
        for i in range(len(constantes)):
            if ( constantes[i] == curva ):
                index_file = i
                break
        
        lista_puntos = self.leer_curva(curvas_in[index_file].replace("Curvas/", "/home/valen/PPS/MIDE3700/tests/Suavisar/Output_Suavisar/"))
        
        return lista_puntos

    def graficar_punto(self, axes, xy, color="red", marker="x"):
        plt.scatter([xy[0]],[xy[1]],color=color, marker="x", s=100)

    def elegir_derecha(self, xy, p1, p2):
        """
        Dado un punto (x, y), devuelve True si p1, esta más cerca que p2 a (x, y)
        """

        x1 = xy[0]
        y1 = xy[1]
        x2 = p1[0]
        y2 = p1[1]

        distancia_p1 = distancia_euclidea(x1, x2, y1, y2)

        x2 = p2[0]
        y2 = p2[1]

        distancia_p2 = distancia_euclidea(x1, x2, y1, y2)

        return distancia_p1 < distancia_p2

    def buscar_medio(self, xy, c1, curvas_in = None, curva1 = None, curva2 = None):
        """
        Dada unas coordenadas x e y, retorna el indice de la curva que más se acerca al punto
        """
        #Busco en los archivos las 2 curvas, con las coordenadas x e y de cada punto 

        #Mientras no encuentre la distancia minima, buscar

        index_curva = int(len(c1)/2)
        largo_segmento = int(len(c1)/2)
        umbral_busqueda = int((len(c1)/100) * 10)
        
        punto_actual = c1[index_curva]
        punto_der = c1[index_curva-1]
        
        mover_derecha = self.elegir_derecha(xy, punto_actual, punto_der)

        punto_anterior = punto_actual

        # self.graficar_punto(axes, punto_actual)
        # self.graficar_punto(axes, xy)
        # self.graficar_punto(axes, c1[0], color="green")

        #Mientras el tamaño del segmento no sea lo suficientemente pequeño sigo buscando
        #Pequeño será el 5% del total de los puntos en la curva
        
        while (largo_segmento > umbral_busqueda):

            largo_segmento /= 2
            punto_anterior = punto_actual
            #Buscar a derecha
            if mover_derecha:
                index_curva = int(index_curva + largo_segmento)

                punto_actual = c1[index_curva]
                punto_der = c1[index_curva-1]

            #Buscar a la izquierda
            else:
                index_curva = int(index_curva - largo_segmento)

                punto_actual = c1[index_curva]
                punto_der = c1[index_curva-1]

            mover_derecha = self.elegir_derecha(xy, punto_actual, punto_der)

            # self.graficar_curvas(curvas_in, [curva1, curva2], axes)
            # self.graficar_punto(axes, xy, color="blue")
            # self.graficar_punto(axes, punto_anterior, color="green")
            # self.graficar_punto(axes, punto_actual, color="red")

            # plt.draw()
            # plt.show()
        medio = int( punto_actual[2] )

        return medio
    
    def fijar_rango(self, medio, curva_completa):
        inicio  = medio - int( (len( curva_completa ) / 10) )
        if inicio < 0:
            inicio = 0

        fin     = medio + int( (len( curva_completa ) / 10) * 2 )
        if fin > len( curva_completa ):
            fin = len( curva_completa )

        return inicio, fin
    
    def calcular_minimas_distancias_entre_curvas(self, xy, curvas_in, curva1, curva2):
        """
        Esta función, dado:
        xy: un par con coordenadas x e y en el plano
        curvas_in: la lista de archivos que contienen las curvas almacenadas en conjuntos de puntos x,y
        curva1 y curva2, contienen el valor constante que representa la curva, una curva en el planto es un conjunto de puntos x,y -> z, donde z es el valor constante
        """
        
        # fig, axes = plt.subplots()
        # self.graficar_curvas(curvas_in, [curva1, curva2], axes)
        
        c1 = self.get_puntos_curva(curvas_in, curva1)
        c2 = self.get_puntos_curva(curvas_in, curva2)

        curva_completa = self.get_puntos_curva_completa(curvas_in, curva1)
        curva_2_completa = self.get_puntos_curva_completa(curvas_in, curva2)

        medio = self.buscar_medio(xy, c1, curvas_in)

        inicio, fin = self.fijar_rango(medio, curva_completa)

        medio = self.buscar_medio(xy, c2, curvas_in)

        inicio_2, fin_2 = self.fijar_rango(medio, curva_2_completa)
        
        dist1 = calcular_min_distance(xy, curva_completa[inicio:fin])
        dist2 = calcular_min_distance(xy, curva_2_completa[inicio_2:fin_2])
        
        # minima_distancia = calcular_min_distance(xy, curva_completa)      
        
        if True:
        #     plt.title(f"Caso {xy[0]} {xy[1]}")
            self.graficar_punto(axes,xy, color="black",marker="o")
            # self.graficar_punto(axes,curva_completa[medio], color="green")
            # plt.draw()
            # plt.show()
        #     # plt.savefig(f"/home/valen/Casos_MIDE3700/Versión nueva/{xy[0]},{xy[1]}.png")
        return dist1, dist2
    
    def buscar_curvas(self, x, y):
        print("buscar_curvas: ", x,y)
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
        
        x = Algebra.Redondeo_int_mas_cerca(x)
        y = Algebra.Redondeo_int_mas_cerca(y)
        print("ahora valen; ", x, y)
        valor_en_matriz = str(self.matriz[x][y])
            

        print("valor en matriz: ", valor_en_matriz)
    
        curvas_in = self.Leo_Archivo()
        titulo = self.nombrar_archivo(curvas_in)
        
        dict_curvas = curves[titulo]
        entre_curvas = dict_curvas[valor_en_matriz]
                    
        return entre_curvas
            
    #Interpolo versión 2 con matriz rellenada:
    def Entre_que_curvas_esta_el_punto_x_e_y(self, x, y):
        i1, i2, xx, j1, j2, yy = self.Parametrizar(x, y)
        
        
        #buscar_curvas devuelve un diccionario: 
        #  {curva_1 :  (valor Constante, posición en las curvas),
        #  curva_2 :  (valor Constante, posición en las curvas),}
        curve_1, curve_2 = self.buscar_curvas(xx, yy)
        
        lohice = True
        magnitud = 0
        extrapolo = False
        # return lohice, magnitud, extrapolo
    
    def Interpolo(self, x, y):
        magnitud_nueva = 99999.
        # self.Entre_que_curvas_esta_el_punto_x_e_y(x, y)
        # Parametrizamos el eje x y la cordenada x del punto

        if self.x0 >= 0.:
            i1= Algebra.Redondeo_int_mas_cerca( self.x0 * float(self.kx) )
            i2= Algebra.Redondeo_int_mas_cerca( self.xn * float(self.kx) )
            xx= x * float(self.kx)
        else:
            i1= 0
            i2= Algebra.Redondeo_int_mas_cerca( (self.xn + abs(self.x0)) * float(self.kx) )
            xx= (x + abs(self.x0)) * float(self.kx)

        # Parametrizamos el eje y y la coordenada y del punto

        if self.y0 >= 0.:
            j1= Algebra.Redondeo_int_mas_cerca( self.y0 * float(self.ky) )
            j2= Algebra.Redondeo_int_mas_cerca( self.yn * float(self.ky) )
            yy= y * float(self.ky)
        else:
            j1= 0
            j2= Algebra.Redondeo_int_mas_cerca( (self.yn + abs(self.y0)) * float(self.ky) )
            yy= (y + abs(self.y0)) * float(self.ky)

        # Lo que vamos a hacer es buscar los 3 puntos más cercanos
        # al punto (xx,yy), 
        # sobre tres curvas distintas y consecutivas.

        # Primero busco la curva de nivel mas cercana al punto

        # print(f"valores de entrada: {i1} <= {xx} and {xx} <= {i2} and {j1} <= {yy} and {yy} <= {j2}")
        if i1 <= xx and xx <= i2 and j1 <= yy and yy <= j2:
            dist_min_1= 1000.

            #Comparo las distancias de cada punto en la matriz
            for i in range(i1,i2):
                for j in range(j1,j2):

                    if self.matriz[i][j] != 99999.:
                        #Calculo la distancia euclidea
                        # ( un valor * 100 - x * 100 ) ** 2
                        #  un valor de 0-58 * 100 - ( x + (algo) * 100  ) **2 -> (100 * ( un valor de 0-58 - (x+algo))) **2
                        # (100) **2 * (un valor 0-58 - (x+algo)) **2
                        # (100)*100 * (un valor 0-58 - (x+algo)) **2
                        di = (float(i) - xx) * (float(i) - xx)/ float(self.kx)/ float(self.kx)
                        dj = (float(j) - yy) * (float(j) - yy)/ float(self.ky)/ float(self.ky)
                        dist= math.sqrt(di + dj)

                        if dist < dist_min_1:
                            dist_min_1= dist
                            cte_1= self.matriz[i][j]
                            x1= float(i) / float(self.kx)
                            y1= float(j) / float(self.ky)

            # print(f"\n\n -------------------------- \n x: {xx}\n y: {yy} \n{dist_min_1} \n--------------------------\n\n")
            key= True
            i= 0

            #Busco a que curva pertence el punto más cercano
            while key:
                if cte_1 == self.cte_curvas[i]:
                    n1= i
                    key= False
                else:
                    i += 1

            # Ahora busco el punto mas cercano en las curvas anterior y siguiente

            #Si no es la primer ni la última curva -> Esta entre 2 curvas
            if n1 != 0 and n1 != (self.nc - 1):
                dist_min_2= 1000.
                dist_min_3= 1000.
                for i in range(i1,i2):
                    for j in range(j1,j2):
                        if self.matriz[i][j] == self.cte_curvas[n1-1]:
                            di= (float(i) - xx) * (float(i) - xx)/ float(self.kx)/ float(self.kx)
                            dj= (float(j) - yy) * (float(j) - yy)/ float(self.ky)/ float(self.ky)
                            dist= math.sqrt(di + dj)

                            if dist < dist_min_2:
                                dist_min_2= dist
                                cte_2= self.matriz[i][j]
                                x2= float(i) / float(self.kx)
                                y2= float(j) / float(self.ky)

                        if self.matriz[i][j] == self.cte_curvas[n1+1]:
                            di= (float(i) - xx) * (float(i) - xx)/ float(self.kx)/ float(self.kx)
                            dj= (float(j) - yy) * (float(j) - yy)/ float(self.ky)/ float(self.ky)
                            dist= math.sqrt(di + dj)

                            if dist < dist_min_3:
                                dist_min_3= dist
                                cte_3= self.matriz[i][j]
                                x3= float(i) / float(self.kx)
                                y3= float(j) / float(self.ky)


                # Ahora hay que ver si el punto se encuentra entre las curvas
                # n1 y n1+1 o entre las curvas n1 y n1-1.
                # Para definir esto calculamos las distancias entre los puntos
                # (x1, y1) y (x2, y2) y entre los puntos (x1, y1) y (x3, y3):

                d1= (x1 - x2) * (x1 - x2)
                d2= (y1 - y2) * (y1  - y2)
                dist_12= math.sqrt(d1 + d2)

                d1= (x1 - x3) * (x1 - x3)
                d2= (y1 - y3) * (y1  - y3)
                dist_13= math.sqrt(d1 + d2)

                # Ahora, si el punto (X,Y) se encuentra entre las curvas
                # n1-1 y n1 tendremos que
                
                #    dist_12 > dist_min_2  y  dist_13 < dist_min_3

                # en cambio, si el punto se encuentra entre las curvas ni y ni+1

                #  dist_13 > dist_min_3  y  dist_12 < dist_min_2

                curvas_in = self.Leo_Archivo()
                titulo = self.nombrar_archivo(curvas_in)
                # print(titulo)
                
                curva1, curva2 = self.buscar_curvas(xx, yy)
                distancia_1, distancia_2 = self.calcular_minimas_distancias_entre_curvas((x, y), curvas_in, curva1, curva2)
                
                #Mostrar punto más cercano encontrado del primer algoritmo:
                # print(f"- Nuevo: {curva1}  dist = {distancia1}")

                #Calculo la nueva magnitud:
                distancia_entre_curvas = distancia_1 + distancia_2
                magnitud_nueva = curva1 - distancia_1 * (curva1 - curva2) / distancia_entre_curvas
                    
                print(f"Magnitud: {magnitud_nueva:.4} = {curva1} - {distancia_1:.4} * ({curva1} - {curva2}) / {distancia_1:.4} + {distancia_2:.4}")

                #Compruebo que la suma de las distancias sea 1
                # d1 = distancia_1/distancia_entre_curvas
                # d2 = distancia_2/distancia_entre_curvas
                # print(d1 + d2, d1 + d2 == 1)


                if dist_12 > dist_min_2 and dist_13 < dist_min_3:
                    # print(f"Metodo viejo para curva 1: {cte_1} dist = {dist_min_1}|{dist_min_2}")
                    # output.write(f" {dist_min_1}")
                        # La distancia entre las curvas a la altura del punto es
                    dist_min= dist_min_1 + dist_min_2
                    magnitud= cte_1 - dist_min_1*(cte_1 - cte_2)/dist_min

                    # #Calculo la nueva magnitud:
                    # distancia_entre_curvas = distancia_1 + distancia_2
                    # resta = distancia_1 * (cte_1 - cte_2) / distancia_entre_curvas
                    # magnitud_nueva = curva1 - distancia_1 * (curva1 - curva2) / ditancia_entre_curvas

                    # print(f"Los valores de magnitud son: \n {cte_1} - {dist_min_1}*({cte_1} - {cte_2})/{dist_min} " )
                    # print(f"Los valores nuevos son: \n {cte_1} - {distancia_1} * ({cte_1} - {cte_2}) / {distancia_entre_curvas}" )
                    # print(f"Magnitud: {magnitud_nueva} = {cte_1} - {distancia_1} * ({cte_1} - {cte_2}) / {distancia_1} + {distancia_2}, la resta es {resta}")
                    #Compruebo que la diferencia sea 0
                    # print(f"La diferencia entre magnitudes es: {magnitud} - {magnitud_nueva} ={magnitud - magnitud_nueva}")

                    #Reviso las diferencias
                    # print(f"los valores de la distancias son: {dist_min} - {distancia_entre_curvas} = {dist_min-distancia_entre_curvas}")
                    # print(f"distancias {dist_min_1} - {distancia_1} = {dist_min_1 - distancia_1}")

                else:
                    # print(f"Metodo viejo para curva 1: {cte_1} , dist = {dist_min_1}|{dist_min_3}")
                    # output.write(f" {dist_min_1}")
                    dist_min= dist_min_1 + dist_min_3
                    magnitud= cte_3 - dist_min_3*(cte_3 - cte_1)/dist_min

                    # #Calculo la nueva magnitud:
                    # ditancia_entre_curvas = distancia_1 + distancia_2
                    # magnitud_nueva = curva1 - distancia_1 * (curva1 - curva2) / ditancia_entre_curvas
                    
                    # print(f"Magnitud: {magnitud_nueva} = {curva1} - {distancia_1} * ({curva1} - {curva2}) / {distancia_1} + {distancia_2}")
                    # #Compruebo que la diferencia sea 0
                    # print(f"La diferencia entre magnitudes es: {magnitud - magnitud_nueva}")
                
                extrapolo= False
                lohice= True

            #Si es la primer curva, el punto más cercano esta en el valor que tiene n+1, que es 1
            elif n1 == 0:
                dist_min_3= 1000.
                for i in range(i1,i2):
                    for j in range(j1,j2):
                        if self.matriz[i][j] == self.cte_curvas[n1+1]:
                            di= (float(i) - xx) * (float(i) - xx)/ float(self.kx)/ float(self.kx)
                            dj= (float(j) - yy) * (float(j) - yy)/ float(self.ky)/ float(self.ky)
                            dist= math.sqrt(di + dj)

                            if dist < dist_min_3:
                                dist_min_3= dist
                                cte_3= self.matriz[i][j]
                                x3= float(i) / float(self.kx)
                                y3= float(j) / float(self.ky)

                d1= (x1 - x3) * (x1 - x3)
                d2= (y1 - y3) * (y1 - y3)
                dist_13= math.sqrt(d1 + d2)
                dist_min= dist_min_1 + dist_min_3

                # Si dist_13 > dist_min_3 el punto esta entre las curvas n1 y n1+1

                magnitud= cte_3 - dist_min_3 * (cte_3 - cte_1) / dist_13

                if dist_13 > dist_min_3:
                    #magnitud= cte_3 - dist_min_3 * (cte_3 - cte_1) / dist_min
                    extrapolo= False
                else:
                    #magnitud= cte_3 + dist_min_3 * (cte_3 - cte_1) / dist_13
                    extrapolo= True
                lohice= True

            #Si es la última curva
            elif n1 == (self.nc - 1):
                dist_min_2= 1000.
                for i in range(i1,i2):
                    for j in range(j1,j2):
                        if self.matriz[i][j] == self.cte_curvas[n1-1]:
                            di= (float(i) - xx) * (float(i) - xx)/ float(self.kx)/ float(self.kx)
                            dj= (float(j) - yy) * (float(j) - yy)/ float(self.ky)/ float(self.ky)
                            dist= math.sqrt(di + dj)

                            if dist < dist_min_2:
                                dist_min_2= dist
                                cte_2= self.matriz[i][j]
                                x2= float(i) / float(self.kx)
                                y2= float(j) / float(self.ky)

                d1= (x1 - x2) * (x1 - x2)
                d2= (y1 - y2) * (y1 - y2)
                dist_12= math.sqrt(d1 + d2)
                dist_min= dist_min_1 + dist_min_2

                # Si dist_12 > dist_min_2 el punto esta entre las curvas n1 y n1-1

                magnitud= cte_1 + dist_min_1 * (cte_1 - cte_2) / dist_12
                
                if dist_12 > dist_min_2:
                    #magnitud= cte_1 + dist_min_1 * (cte_1 - cte_2) / dist_min
                    extrapolo= False
                else:
                    #magnitud= cte_2 + dist_min_2 * (cte_2 - cte_1) / dist_12
                    extrapolo= True
                lohice= True

        else:
            print("Calcula Fallido")
            extrapolo= False
            lohice= False
            magnitud= 99999.
            magnitud_nueva = 99999.

        return lohice, magnitud_nueva, extrapolo
#-------------------------------------------------------------------------------
    def Error(self, D, L, M):
#
# El error de medicion en D es 0.02
# El error de medicion en lambda_1 es 2
#
        err_D= 0.02
        #err_L= 10.
        err_L= 2.
#
        D1= D + err_D
        D2= D - err_D
#
        L1= L + err_L
        L2= L - err_L
#
# Calculo el valor de la magnitud con los nuevos valores D1, D2, L1 y L2
#
        lohice1, m1, extra1= self.Interpolo(D1, L1)
        lohice2, m2, extra2= self.Interpolo(D1, L2)
        lohice3, m3, extra3= self.Interpolo(D2, L1)
        lohice4, m4, extra4= self.Interpolo(D2, L2)
#
# Ahora promediamos los valores de los errores
#
        n= 0
#
        if lohice1:
            err1= abs(M - m1)
            n= n + 1
        else:
            err1 = 0.0
#
        if lohice2:
            err2= abs(M - m2)
            n= n + 1
        else:
            err2= 0.0
#
        if lohice3:
            err3= abs(M - m3)
            n= n + 1
        else:
            err3= 0.0
#
        if lohice4:
            err4= abs(M - m4)
            n= n + 1
        else:
            err4= 0.0
#
        error= (err1 + err2 + err3 + err4) / float(n)

#
        return error
#-----------------------------------------------------------------------------------------

