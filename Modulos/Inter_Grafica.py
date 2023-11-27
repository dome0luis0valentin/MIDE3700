#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
# Sacado de la pagina 
# http://scienceoss.com/interactively-select-points-from-a-plot-in-matplotlib/
################################################################################
from pylab import *
import math
import matplotlib.pyplot as plt
import numpy as np
import Espectro

import Polinomios
import copy
from Funciones_auxiliares import encontrar_punto_mas_cercano, encontrar_punto_mas_cercano_normalizado, encontra_aproximado_eje_x
from Funciones_auxiliares import calcular_indice_del_punto_mas_cercano

from Modulos.Punto import Punto
################################################################################
################################################################################
################################################################################
class Inter_Grafica:

# Atributos de la clase

    event = None
    xdatalist = [] # coordenadas x de puntos a ajustar
    ydatalist = [] # coordenadas y de puntos a ajustar
    p = Polinomios.Polinomio() # polinomio de ajuste
    archivo= ""
    nor= bool # es para saber si el espectro esta normalizado
    key1= True
    key2= True
    espectro = None #Recibe las coordenadas x e y del espectro

#Atributos para el manejo de colores de las rectas y curvas
    colores = ['b', 'g', 'r', 'c', 'm', 'y', 'k'] #Es el color actual de la curva
    index_color_actual = 0
#Lista de puntos en el gráfico, funciona de forma independiente de xdatalist e ydatalist
    points = []
#-------------------------------------------------------------------------------
    def __init__(self, archivo, nor, espectro):
#        self.archivo= "Ajustes/" + nombre + ".out" # Archivo de salida
        self.archivo= archivo
        self.xdatalist = [] # puntos a ajustar
        self.ydatalist = []
        self.p.coef= []
        self.nor= nor
        self.espectro = espectro
#-------------------------------------------------------------------------------
    def click(self, event):
        import Modulos
        self.event = event

#
# Con el boton izquierdo agrego un punto
        if event.button == 1:
#
            clic_x = event.xdata
            clic_y = event.ydata


#Normalizo los datos para poder trabajar con el gráfico en iguales dimencioenes de 0 a 1
            if isinstance(self.espectro, Modulos.Normalizo_espectro.Normalizo_espectro):
                eje_y_normalizado = []
                
                for i in self.espectro.flujo:
                    eje_y_normalizado.append(math.log(i,10))
                
                eje_x = self.espectro.l_onda

                x, y = encontra_aproximado_eje_x(clic_x, clic_y, eje_x, eje_y_normalizado)

            else:
                max_x = max(self.espectro.l_onda)
                max_y = max(self.espectro.log_flujo)

                eje_x_normalizado = [v / max_x for v in self.espectro.l_onda]
                eje_y_normalizado = [v / max_y for v in self.espectro.log_flujo]            
                    
                x, y = encontrar_punto_mas_cercano(clic_x/max_x, clic_y/max_y, eje_x_normalizado, eje_y_normalizado)
                #Desnormalizo la coordenada
                x = x*max_x
                y = y*max_y

            #Agrego el punto a la lista de puntos
 
            self.xdatalist.append(x)
            self.ydatalist.append(y)
           
            ax = gca()  # mantengo los ejes actuales

            # Graficamos un punto rojo en el punto del espectro más cercano.
            new_point = ax.plot([x],[y],'ro', picker=5)
            
            self.agregar_punto(Punto(x, y, new_point[0]))
            draw()  # refrescamos el grafico.

#
# Con el boton derecho, busco el más cercano, si el más cercano esta activo --> Lo desactivo
#                                               si el más cercano esta inactivo --> Lo activo
#
        if event.button == 3:

            clic_x = event.xdata
            clic_y = event.ydata
            coor_x= self.xdatalist
            coor_y= self.ydatalist
            indice_mas_cercano = calcular_indice_del_punto_mas_cercano(clic_x, clic_y, coor_x, coor_y)
           

            if indice_mas_cercano == -1:
                return
            print(indice_mas_cercano)
            
            punto = self.points[indice_mas_cercano]
            
            print("Este es el punto más cercano: Type:  ", type(punto), punto.x, punto.y)
            if punto.get_activate():
                punto.set_activate(False)
                punto.set_color("grey")
                #desactivo y pinto de gris
            else:
                punto.set_activate(True)
                punto.set_color("red")
                #activo y pinto de verde

            ax = gca()  # mantengo los ejes actuales
           
            #ax.plot(x[i_min],y[i_min],'kx',lw=2,ms=12)
            
            draw()
#
        else: return
        """
#
#     Busco el punto más cercano
            dif_min= abs(x[0] - event.xdata)
            for j in range(len(x)):
                dif= abs(x[j] - event.xdata)
                if dif <= dif_min:
                    dif_min= dif
                    i_min= j
#
            self.xdatalist= []
            self.ydatalist= []
#
            for j in range(len(x)):
                if j != i_min:
                    self.xdatalist.append( x[j] )
                    self.ydatalist.append( y[j] )

        """           
          
#
#-------------------------------------------------------------------------------
    def ajuste_recta(self, event):
#
        if event.key not in ('a','q'): return
        if event.key=='a':
#
            #Armo la recta sobre los puntos que estan activos
            x_active = []
            y_active = []
            
            for point in self.get_puntos():
                if point.get_activate():
                    x_active.append(point.x)
                    y_active.append(point.y)
                    
            print(f'Estos son los puntos a ajustar en la recta:')
            for i in x_active:
                print(i)
                                
            ajuste= self.p.minimos_cuadrados(x_active,y_active,1)
#

            color = self.cambiar_color()

            if ajuste:
                y= poly1d(self.p.coef); y
                x= []
                if self.nor:
                    x.append(1./3700.)
                else:
                    x.append(3700.)
                for i in self.xdatalist:
                    x.append(i)
#
                x.sort()
                
                ax= gca()  # mantengo los ejes actuales
                #obsoleto: ya no es necesario MatplotLib lo hace por defecto
                #ax.hold(True) # superpongo graficos.
                
                ax.plot(x,polyval(y,x), color+'-')
                draw()
#
                self.Print_puntos('recta')
            else:
                n= 1 - ( len(self.xdatalist) ) + 2
                while self.key1:
                    if n == 1:
                        texto= 'Agregue 1 punto \ Add 1 point'
                        plt.figtext(0.50, 0.85, texto)
                        draw()
                    else:
                        texto= 'Agregue ' + str(n) + ' puntos \ Add ' + str(n) + ' points'
                        plt.figtext(0.50, 0.85, texto)
                        draw()
                    self.key1= False
#
        else:
            plt.close(event.canvas.figure)
            return
#-------------------------------------------------------------------------------
    def ajuste_parab(self, event):
        if event.key not in ('a','q'): return
        if event.key=='a':
#                
            x_active, y_active = self.get_active_points()

            ajuste= self.p.minimos_cuadrados(x_active,y_active,2)         
#   
            color = self.cambiar_color()   

            if ajuste:
                y= poly1d(self.p.coef); y
                x= []
                if self.nor:
                    x.append(1./3700.)
                else:
                    x.append(3700.)
                for i in x_active:
                    x.append(i)
#
                x.sort()
                
                ax= gca()  # mantengo los ejes actuales
                #obsoleto: ya no es necesario MatplotLib lo hace por defecto
                #ax.hold(True) # superpongo graficos.                
                
                ax.plot(x,polyval(y,x), color+'-')                

                draw()
#
                self.Print_puntos('parabola')
            else:
                n= 2 - ( len(self.xdatalist) ) + 2
                while self.key2:
                    if n == 1:
                        texto= 'Agregue 1 punto \ Add 1 point'
                        plt.figtext(0.50, 0.85, texto)
                        draw()
                    else:
                        texto= 'Agregue ' + str(n) + ' puntos \ Add ' + str(n) + ' points'
                        plt.figtext(0.50, 0.85, texto)
                        draw()
                    self.key2= False
#
        else:
            plt.close(event.canvas.figure)
# Guardo los valores
            self.Print_pol('parabola')
            return
#-------------------------------------------------------------------------------
    def Print_puntos(self, fun):
        f= open(self.archivo, "a")
        f.write( 'Puntos ajustados\n' )
        
        #Escribo solamente los puntos que no estan activos:
        x_active, y_active = self.get_active_points()
        
        for i in range(len(x_active)):
            f.write( 'x = %s and y = %s' % (x_active[i],y_active[i]))
            f.write('\n')
#
        y= self.p.Print_pol(self.p)
        if fun == 'recta':
            f.write('Recta: ' + '%s' %y + '\n')
        else:
            f.write( 'Parabola: ' + '%s' %y + '\n' )
        f.close()
        return
#-------------------------------------------------------------------------------
    def Print_pol(self, fun):
        f= open(self.archivo, "a")
        y= self.p.Print_pol(self.p)
        f.write( '===========================================\n' )
        f.write( 'Guardamos el ajuste\n' )
        f.write( 'Save the fit\n' )
        if fun == 'recta':
            f.write( 'Recta: ' + '%s' %y + '\n')
        else:
            f.write( 'Parabola: ' + '%s' %y + '\n')
        f.write( '===========================================\n' )
        f.write( '\n' )
        f.close()
        return
#-------------------------------------------------------------------------------
    def cambiar_color(self, index_color=None):
        """
        Modifico el color actual de la curva
        """
        if index_color is not None:
            self.index_color_actual = index_color
        else:
            self.index_color_actual += 1

        color = self.colores[self.index_color_actual % len(self.colores)]

        return color
    
 #-------------------------------------------------------------------------------
    def agregar_punto(self, punto):
        self.points.append(punto)

    def get_puntos(self):
        return self.points
    
    def clean_puntos(self):
        self.points = []

    def get_active_points(self):
        x_active = []
        y_active = []
        for point in self.get_puntos():
            if point.get_activate():
                x_active.append(point.x)
                y_active.append(point.y)
        return x_active, y_active