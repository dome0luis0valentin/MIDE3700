#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
El programa calcula el flujo emitido por un cuerpo negro de temperatura T.
Divide el espectro de una estrella de temperatura Teff por un espectro de cuerpo negro de la misma temperatura.
"""
import os, sys
import math
import matplotlib.pyplot as plt
from pylab import *
import Espectro
import Polinomios
import Algebra
import Inter_Grafica
import copy
##########################################################################################
# Defino constantes globales
k = 1.3806503 * pow(10.,-16) # erg/K Constante de Boltzmann
c = 2.99792458 * pow(10.,10) # cm/seg  Velocidad de la luz
h = 6.62606876 * pow(10.,-27) # erg seg Constante de Planck
pi = math.pi
#
c1 = 2. * h * (c**2)
c2 = (h * c)/k
##########################################################################################
class Normalizo_espectro(Espectro.Espectro):
# Hereda la clase Espectro
#
    T= int()# temperatura del cuerpo negro
    espectro= Espectro.Espectro(str())# es el espectro de la estrella
#
# espectro normalizado de la estrella
#
    nombre= ""
    archivo_out= ""
    l_onda= []
    flujo= []
    paschen= Polinomios.Polinomio()
    balmer= Polinomios.Polinomio()
    balmer_inf= Polinomios.Polinomio()
    xP= []
    yP= []
    xB= []
    yB= []
    xB_inf= []
    yB_inf= []
    xH_inf= []
    yH_inf= []
#-------------------------------------------------------------------------------
    def __init__(self, T, espectro):
#
# Inicializo los valores
#
        self.espectro= espectro
        self.T= T + 2000
#
        self.nombre= 'Normalized' + espectro.nombre
        self.archivo_out= espectro.archivo_out
#
        self.l_onda= []
        self.flujo= []
        self.paschen= Polinomios.Polinomio()
        self.balmer= Polinomios.Polinomio()
        self.balmer_inf= Polinomios.Polinomio()
        self.balmer_sup= Polinomios.Polinomio()
        self.paschen.grado= 1
        self.balmer.grado= 1
        self.balmer_inf.grado= 2
        self.xP= []
        self.yP= []
        self.xB= []
        self.yB= []
        self.xB_inf= []
        self.yB_inf= []
        self.xH_inf= []
        self.yH_inf= []
#
        f_est= open(self.archivo_out, "a") # Archivo de salida
        f_est.write( '\n' )
        f_est.write( '################################\n' )
        f_est.write( 'NORMALIZO EL ESPECTRO\n' )
        f_est.write( 'SPECTRUM NORMALIZATION\n' )
        f_est.write( '--------------------------------\n' )
        f_est.write( '\n' )
        f_est.close()
#
        return
#-----------------------------------------------------------------------------------------
    def Normalizo(self):
        """
        El flujo emitido por un cuerpo negro es igual a

        F = pi . B = (C1 / lambda^{5})/(exp^{C2/lambda . T} - 1)

        donde

        C1 = 2 pi h c^{2} = 3.7412 x 10^{-5} erg cm^{-2} seg^{-1} (lambda en cm)

        C2 = hc/k = 1.43879 cm ºK

        Para normalizar el espectro del cuerpo negro tenemos que encontrar el
        valor maximo del flujo. Para esto utilizamos la ley de Wien

        Lambda_max * T = 0.28978 cm ºK

        Luego con al valor de Lambda_max se calcula el valor del flujo 
        correspondiente, B_max
        """
#
        lambda_max, b_max= self.Ley_Wien()
#
#     Para cada longitud de onda del espectro, calculamos el flujo de cuerpo negro
#
        k= 0
        for i in self.espectro.l_onda:
            lambda_cm= i * pow(10.,-8) # paso a cm
            b_lambda= (c1 / pow(lambda_cm,5))/(math.exp(c2/(lambda_cm * self.T)) - 1.)
#
# Asi el flujo astrofisico estara en unidades de ergs/cm**2/s/A
#
            b_lambda= (b_lambda * pow(10.,-8)) * 4. * pi 
#
#     El flujo normalizado de cuerpo negro es
#
            b_nor= b_lambda / b_max
#
#     Divido el flujo del espectro por el del cuerpo negro normalizado
#
            self.l_onda.append( 1. / i ) # en Angstroms
            self.flujo.append( self.espectro.flujo[k] / b_nor )
            k= k + 1
#
        return
#-----------------------------------------------------------------------------------------
    def Ley_Wien(self):
        """
        Segun la ley de Wien

        Lambda_max * T = 0.28978 cm ºK
        """
#
        lambda_max = 0.28978 / self.T  #lambda en cm
#
        b_max = (c1 / pow(lambda_max,5))/(math.exp(c2/(lambda_max * self.T)) - 1.)
        b_max = (b_max * pow(10.,-8))* 4. * pi
#
#     El flujo esta en erg/cm**2/seg/A
#
        return lambda_max, b_max
#-----------------------------------------------------------------------------------------
    def Grafico_espec(self, n):
#
        # n= 1  Grafico el espectro
        # n= 2  Grafico el espectro y Paschen
        # n= 3  Grafico el espectro, Paschen, Balmer y Balmer inf
#
        log_flujo= []
        for i in self.flujo:
            log_flujo.append( math.log(i,10) )
#
    # Graficamos el espectro
#
        plt.xlabel('$1/ \lambda$ [$\AA$]')
        plt.ylabel('$\log (F_{\lambda} / B_{\lambda})$')
        plt.plot(self.l_onda, log_flujo, 'b-')
        plt.axvline(x=1./3700., color='k')
#
# Grafico los ajustes realizados hasta el momento
#
        if n >= 2:
            yp= poly1d(self.paschen.coef); yp
            xp= []
            for i in self.l_onda:
                if i < 1./3700.:
                    xp.append( i )
            plt.plot(xp, polyval(yp,xp), 'g-')# Grafico Paschen
#
            if n >= 3:
                yb= poly1d(self.balmer.coef); yb
                xb= []
                for i in self.l_onda:
                    if i > 1./3700.:
                        xb.append( i )
                plt.plot(xb, polyval(yb,xb), 'g-')# Grafico Balmer
                if n == 3:
                    plt.plot(self.xB_inf, self.yB_inf, 'ro')
                    plt.title(self.nombre + '\n' + 'Ajuste la envolvente inferior\n' + 'Fit the bottom envelope of Balmer lines')
            else:
                plt.plot(self.xB, self.yB, 'ro')
                plt.title(self.nombre + '\n' + 'Ajuste el continuo de Balmer\n' + 'Fit the Balmer continuum')
        else:
            plt.plot(self.xP, self.yP, 'ro')
            plt.title(self.nombre + '\n' + 'Ajuste el continuo de Paschen\n' + 'Fit the Paschen continuum')
            
        plt.show()
#-------------------------------------------------------------------------------
    def Ajuste_Paschen(self):
#
        f_est= open(self.archivo_out, "a") # Archivo de salida
        f_est.write( '\n' )
        f_est.write( 'AJUSTE DEL CONTINUO DE PASCHEN\n' )
        f_est.write( 'FIT OF THE PASCHEN CONTINUUM\n' )
        f_est.write( '------------------------------\n' )
        f_est.write( '\n' )
        f_est.close()
#
#     Traemos los puntos con los que hicimos el ajuste
#
        for i in self.espectro.xP:
            k, x= Algebra.Busco_elemento(self.l_onda, 1./i)
            self.xP.append( x )
            self.yP.append( math.log( self.flujo[k],10) )
            
        ajuste= Inter_Grafica.Inter_Grafica(self.archivo_out, True)
        ajuste.xdatalist= copy.copy( self.xP )
        ajuste.ydatalist= copy.copy( self.yP )

        Inter_Grafica.connect('button_press_event', ajuste.click)
        Inter_Grafica.connect('key_press_event', ajuste.ajuste_recta)
        self.Grafico_espec(1)
        self.paschen.coef= copy.copy( ajuste.p.coef )
#
        return
#-------------------------------------------------------------------------------
    def Ajuste_Balmer(self):
#
        f_est= open(self.archivo_out, "a") # Archivo de salida
        f_est.write( '\n' )
        f_est.write( 'AJUSTE DEL CONTINUO DE BALMER\n' )
        f_est.write( 'FIT OF THE BALMER CONTINUUM\n' )
        f_est.write( '------------------------------\n' )
        f_est.write( '\n' )
        f_est.close()
#
#     Traemos los puntos con los que hicimos el ajuste
#
        for i in self.espectro.xB:
            k, x= Algebra.Busco_elemento(self.l_onda, 1./i)
            self.xB.append( x )
            self.yB.append( math.log( self.flujo[k],10) )
#
        ajuste= Inter_Grafica.Inter_Grafica(self.archivo_out, True)
        ajuste.xdatalist= copy.copy( self.xB )
        ajuste.ydatalist= copy.copy( self.yB )
#
        Inter_Grafica.connect('button_press_event', ajuste.click)
        Inter_Grafica.connect('key_press_event', ajuste.ajuste_recta)
        self.Grafico_espec(2)
        self.balmer.coef= copy.copy( ajuste.p.coef )
#
        return
#-------------------------------------------------------------------------------
    def Ajuste_Balmer_inf(self):
#
        f_est= open(self.archivo_out, "a") # Archivo de salida
        f_est.write( '\n' )
        f_est.write( 'AJUSTE DE LA ENVOLVENTE INFERIOR\n' )
        f_est.write( 'FIT OF THE BOTTOM ENVELOPE\n' )
        f_est.write( '------------------------------\n' )
        f_est.write( '\n' )
        f_est.close()
#
#     Traemos los puntos con los que hicimos el ajuste
#
        for i in self.espectro.xB_inf:
            k, x= Algebra.Busco_elemento(self.l_onda, 1./i)
            self.xB_inf.append( x )
            self.yB_inf.append( math.log( self.flujo[k],10) )
#
        ajuste= Inter_Grafica.Inter_Grafica(self.archivo_out, True)
        ajuste.xdatalist= copy.copy( self.xB_inf )
        ajuste.ydatalist= copy.copy( self.yB_inf )
#
        Inter_Grafica.connect('button_press_event', ajuste.click)
        Inter_Grafica.connect('key_press_event', ajuste.ajuste_parab)
        self.Grafico_espec(3)
        self.balmer_inf.coef= copy.copy( ajuste.p.coef )
#
        return
#-------------------------------------------------------------------------------
    def Guardo_ajuste_2(self, BCD):
#
# Genero los polinomios
#
        yp= poly1d(self.paschen.coef); yp
        yb= poly1d(self.balmer.coef); yb
        ybi= poly1d(self.balmer_inf.coef); ybi
#
        xp= []
        xb= []
        xbi= []
#
# Graficamos la envolvente inferior
#
        xv= -self.balmer_inf.coef[1] / (2. * self.balmer_inf.coef[0])
        if xv < 1./3755.:
            min_bi= max(1./3850.,xv)
        else:
            min_bi= 1./3850.
#
        for i in self.l_onda:
            if i <= 1./3700.:
                xp.append( i )
                if i >= min_bi:
                    xbi.append( i )
            else:
                xb.append( i )
#
        log_flujo= []
        for i in self.flujo:
            log_flujo.append( math.log(i,10) )
#
    # Graficamos el espectro
#
        plt.title(self.nombre)
#
        if BCD.D_est > 0.:
            plt.figtext(0.75, 0.85, 'D= %1.2f'%(BCD.D_total))
        else:
            plt.figtext(0.75, 0.85, 'D= ***')
        if BCD.BD2:
            if BCD.D_est > 0.:
                plt.figtext(0.75, 0.70, 'D*= %1.2f'%(BCD.D_est))
            else:
                plt.figtext(0.75, 0.70, 'D*= ***')
            plt.figtext(0.75, 0.65, 'd= %1.2f'%(BCD.d))
#
        f_ajuste2= 'Ajustes/' + self.espectro.nombre + '.2' + '.png'# Nombre del archivo
#
        plt.xlabel('$1/\lambda$ [$\AA$]')
        plt.ylabel('$\log (F_{\lambda}/B_{\lambda})$')
        plt.plot(self.l_onda, log_flujo, 'b-')
        plt.plot(xp, polyval(yp,xp), 'g-')
        plt.plot(xb, polyval(yb,xb), 'g-')
        plt.plot(xbi, polyval(ybi,xbi), 'g-')
        plt.axvline(x=1./3700., color='k')
        plt.savefig(f_ajuste2)
        plt.clf()
#
        return
#-------------------------------------------------------------------------------
