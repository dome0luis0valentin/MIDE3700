#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
import numpy as np
import math
import Algebra
import multiprocessing
from Modulos import Landolt



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
            self.cte_curvas.append( 37. )# => tipo espectral A7
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

        
    #---------------------------------------------------------------------------
    def Matriz_Curvas(self, curvas_in):

        # Parametrizamos el eje x

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
        self.matriz = np.full((i2+1, j2+1), 99999.0, dtype=float)
        # Leo todos los archivos de las curvas

        for i in range(self.nc):
            with open(curvas_in[i], 'r') as f_curva:
                next(f_curva)  # Saltar la primera línea
                for linea in f_curva:

                    xy = [float(j) for j in linea.split() if j]
                    if not self.x0 <= xy[0] <= self.xn or not self.y0 <= xy[1] <= self.yn:
                        continue

                    ii = Algebra.Redondeo_int_mas_cerca((xy[0] + abs(self.x0)) * float(self.kx)) if self.x0 < 0. else Algebra.Redondeo_int_mas_cerca(xy[0] * float(self.kx))
                    jj = Algebra.Redondeo_int_mas_cerca((xy[1] + abs(self.y0)) * float(self.ky)) if self.y0 < 0. else Algebra.Redondeo_int_mas_cerca(xy[1] * float(self.ky))

                    self.matriz[ii][jj] = self.cte_curvas[i]

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
        
        return
    #---------------------------------------------------------------------------
    def Interpolo(self, x, y):

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

        if i1 <= xx and xx <= i2 and j1 <= yy and yy <= j2:
            dist_min_1= 1000.
            for i in range(i1,i2):
                for j in range(j1,j2):
                    if self.matriz[i][j] != 99999.:
                        di= (float(i) - xx) * (float(i) - xx)/ float(self.kx)/ float(self.kx)
                        dj= (float(j) - yy) * (float(j) - yy)/ float(self.ky)/ float(self.ky)
                        dist= math.sqrt(di + dj)

                        if dist < dist_min_1:
                            dist_min_1= dist
                            cte_1= self.matriz[i][j]
                            x1= float(i) / float(self.kx)
                            y1= float(j) / float(self.ky)

            key= True
            i= 0
            while key:
                if cte_1 == self.cte_curvas[i]:
                    n1= i
                    key= False
                else:
                    i += 1

            # Ahora busco el punto mas cercano en las curvas anterior y siguiente

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
                
                if dist_12 > dist_min_2 and dist_13 < dist_min_3:

                    # La distancia entre las curvas a la altura del punto es

                    dist_min= dist_min_1 + dist_min_2
                    magnitud= cte_1 - dist_min_1*(cte_1 - cte_2)/dist_min
                else:
                    dist_min= dist_min_1 + dist_min_3
                    magnitud= cte_3 - dist_min_3*(cte_3 - cte_1)/dist_min

                extrapolo= False
                lohice= True

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
            extrapolo= False
            lohice= False
            magnitud= 99999.

        return lohice, magnitud, extrapolo
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


def cargar_curvas(nombre, curvas_dict):
        curvas = Curvas(nombre)
        curvas_dict[nombre] = curvas
        
def cargar_curvas_multiproceso():
    # Cargo curvas
    # Load curves
    
    # Crear una lista de nombres de curvas
    nombres_curvas = ["Teff", "TE_c", "TE_f", "CL_c", "CL_f", "Logg", "Mv", "Mbol", "PHIo_c", "PHIo_f"]

    # Crear un diccionario para almacenar las curvas
    manager = multiprocessing.Manager()
    curvas_dict = manager.dict()

    # Crear una lista de procesos
    processes = []


    # Crear un proceso para cargar cada curva
    for nombre in nombres_curvas:
        process = multiprocessing.Process(target=cargar_curvas, args=(nombre, curvas_dict))
        processes.append(process)
        process.start()

    # Esperar a que todos los procesos terminen
    for process in processes:
        process.join()

    # Accede a las curvas cargadas por su nombre
    
    # Crear el objeto Landolt
    landolt = Landolt.Landolt()
    
    return curvas_dict, landolt