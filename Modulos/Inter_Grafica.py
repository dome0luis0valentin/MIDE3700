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
from Modulos.Line import Line
from Modulos.Parable import Parable
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
    colores = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#FFA07A', '#00CED1', '#800080'] #Es el color actual de la curva
    index_color_actual = 0
    
#Lista de puntos en el gráfico, funciona de forma independiente de xdatalist e ydatalist
    points = []
    
#Lista con todas las rectas que se van gráficando:
    lines = []
#Lista con todas las parabolas que se van gráficando:
    parables = []   
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

        if event.inaxes != self.espectro.axes:
            return
#
# Con el boton izquierdo agrego un punto
        if event.button == 1:
#
            clic_x = event.xdata
            clic_y = event.ydata
            
            if (clic_x == None or clic_y == None ):
                return

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
            
            ax = self.espectro.axes  # mantengo los ejes actuales

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
            
            punto = self.points[indice_mas_cercano]
            
            if punto.get_activate():
                punto.set_activate(False)
                punto.set_color("grey")
                #desactivo y pinto de gris
            else:
                punto.set_activate(True)
                punto.set_color("red")
                #activo y pinto de verde

            ax = self.espectro.axes  # mantengo los ejes actuales
           
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
            
            x_active, y_active = zip(*[(point.x, point.y) for point in self.get_puntos() if point.get_activate()])

            ajuste= self.p.minimos_cuadrados(x_active,y_active,1)
#

            if ajuste:
                y= poly1d(self.p.coef); y
                x= []
                if self.nor:
                    x.append(1./3700.)
                else:
                    x.append(3700.)
                    
                x.extend(self.xdatalist) # agrega todos los elementos de self.xdatalist a la lista x
#
                x.sort()
                
                # Utilizo self.axes en lugar de gca()
                color = self.colores[self.index_color_actual]
                self.index_color_actual+=1
                
                line_graph, = self.espectro.axes.plot(x, polyval(y, x), color+'-')
                new_line = Line(grafico = line_graph,
                                x_active = x_active,
                                y_active = y_active)
                draw()
                self.agregar_linea(new_line)
#
                self.Print_puntos('recta')
            else:
                n= 1 - ( len(self.xdatalist) ) + 2
                while self.key1:
                    if n == 1:
                        texto = 'Agregue 1 punto \ Add 1 point'
                        self.espectro.figure.text(0.50, 0.85, texto)
                        draw()
                    else:
                        texto = f'Agregue {n} puntos \ Add {n} points'
                        self.figure.text(0.50, 0.85, texto)
                        draw()
                    self.key1 = False
        else:
            plt.close(self.espectro.figure)
            return
#-------------------------------------------------------------------------------
    def ajuste_parab(self, event):
        if event.key not in ('a','q'): return
        if event.key=='a':
#                
            x_active, y_active = self.get_active_points()

            ajuste= self.p.minimos_cuadrados(x_active,y_active,2)         
#   

            if ajuste:
                y= poly1d(self.p.coef); y
                x= []
                if self.nor:
                    x.append(1./3700.)
                else:
                    x.append(3700.)
                    
                x.extend(x_active)  
#
                x.sort()                
                                
                color = self.colores[self.index_color_actual]
                self.index_color_actual+=1
                
                graph_parable, = self.espectro.axes.plot(x,polyval(y,x), color+'-')
                
                new_parable = Parable(grafico= graph_parable, x_active= x_active, y_active= y_active)
                
                self.agregar_parable(new_parable)
                
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

 #-------------------------------------------------------------------------------

    def agregar_linea(self, linea):
        """
        Agrega el objeto que representa a la linea graficada a la lista de lineas graficadas

        Args:
            linea (_list_): _una lista con un único elemento, que representa a la linea en la interfaz gráfica_
        """
        
        lineas_dibujadas = self.get_lines()
        
        if len(lineas_dibujadas) > 0:
            for l in lineas_dibujadas:
                l.grafico.set_color("gray")
                l.set_last(False)
                
        self.append_line(linea)
        
        self.espectro.create_line_button(self.espectro.axes, 'Ajuste '+str(len(lineas_dibujadas)), lineas_dibujadas, linea)
        
        

    def get_lines(self):
        return self.lines
    
    def append_line(self, line):
        return self.lines.append(line)
    
    def clean_lines(self):
        self.lines = []

    def get_last_line(self):
        lines = []
        for line in self.get_lines():
            if line.is_last():
                lines.append(line)
        return lines
    
    
 #-------------------------------------------------------------------------------
    def agregar_parable(self, parable):
        """
        Agrega el objeto que representa a una parabola graficada a la lista de lineas graficadas

        Args:
            parable (_list_): _una lista con un único elemento, que representa a la parabola en la interfaz gráfica_
        """
        
        parabolas_dibujadas = self.get_parables()
        
        if len(parabolas_dibujadas) > 0:
            for p in parabolas_dibujadas:
                p.set_color("gray")
                
        self.append_parable(parable)
        
        self.espectro.create_parable_button(self.espectro.axes, 'Parabola '+str(len(parabolas_dibujadas)), parabolas_dibujadas, parable)

    def get_parables(self):
        """
        The function returns the parables attribute of an object.
        :return: The method is returning the value of the variable "self.parables".
        """
        return self.parables
    
    def append_parable(self, parable):
        """
        The function appends a parable to a list of parables.
        
        :param parable: The parameter "parable" is a variable that represents a parable. It is being
        passed to the function "append_parable" as an argument
        :return: The method is returning the updated list of parables after appending the new parable.
        """
        return self.parables.append(parable)
    
    def clean_parables(self):
        self.parables = []

    def get_last_parable(self):
        parable = []
        for parable in self.get_parables():
            if parable.is_last():
                self.parables.append(parable)
        return self.parables
    
