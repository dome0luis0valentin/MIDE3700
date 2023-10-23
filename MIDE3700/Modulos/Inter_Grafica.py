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
################################################################################
################################################################################
################################################################################
class Inter_Grafica:

# Atributos de la clase

    event = None
    xdatalist = [] # puntos a ajustar
    ydatalist = []
    p = Polinomios.Polinomio() # polinomio de ajuste
    archivo= ""
    nor= bool # es para saber si el espectro esta normalizado
    key1= True
    key2= True
#-------------------------------------------------------------------------------
    def __init__(self, archivo, nor):
#        self.archivo= "Ajustes/" + nombre + ".out" # Archivo de salida
        self.archivo= archivo
        self.xdatalist = [] # puntos a ajustar
        self.ydatalist = []
        self.p.coef= []
        self.nor= nor
#-------------------------------------------------------------------------------
    def click(self, event):
        self.event = event
#
# Con el boton izquierdo agrego un punto
        if event.button == 1:
#
            self.xdatalist.append(event.xdata)
            self.ydatalist.append(event.ydata)
#
#            print 'x = %s and y = %s' % (event.xdata,event.ydata)
#
            
            ax = gca()  # mantengo los ejes actuales
            #obsoleto: ya no es necesario MatplotLib lo hace por defecto    
            #ax.hold(True) # superpongo graficos.

    # Graficamos un punto rojo dende se hizo click.
            ax.plot([event.xdata],[event.ydata],'ro', picker=5)
            draw()  # refrescamos el grafico.
        if event.button == 3:
#
            x= self.xdatalist
            y= self.ydatalist
#
#     Busco el punto
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
#
            ax = gca()  # mantengo los ejes actuales
            #obsoleto: ya no es necesario MatplotLib lo hace por defecto    
            #ax.hold(True) # superpongo graficos.
            ax.plot(x[i_min],y[i_min],'kx',lw=2,ms=12)
            draw()
#
        else: return
#
#-------------------------------------------------------------------------------
    def ajuste_recta(self, event):
#
        if event.key not in ('a','q'): return
        if event.key=='a':
#
            ajuste= self.p.minimos_cuadrados(self.xdatalist,self.ydatalist,1)
#
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
                
                ax.plot(x,polyval(y,x), 'g-')
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
            ajuste= self.p.minimos_cuadrados(self.xdatalist,self.ydatalist,2)
#
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

                ax.plot(x,polyval(y,x), 'g-')
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
        for i in range(len(self.xdatalist)):
            f.write( 'x = %s and y = %s' % (self.xdatalist[i],self.ydatalist[i]))
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
