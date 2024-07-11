def Redondeo_int_mas_cerca(x):
    """
    Redondea un número al entero más cercano.
    """
    y= ( x - round(x) ) * 10
    if x >= 0.:
        if y < 5.:
            x_int= int( round(x) )
        else:
            x_int= int( round(x) + 1 )
    else:
        if abs(y) < 5.:
            x_int= int( round(x) )
        else:
            x_int= int( round(x) - 1 )        
    return x_int

def Calculo_te(ties):
#
#
        if 6 <= ties <=8:
            if ties < 7:
                n = 6
            else:
                n = 7
        elif 13 <= ties <= 15:
            if ties < 14:
                n = 13
            else:
                n = 14
        elif 15 <= ties <= 17:
            if ties < 16:
                n = 15
            else:
                n = 16
        elif 17 <= ties <= 19:
            if ties < 18:
                n = 17
            else:
                n = 18
        elif 20 <= ties <= 22:
            if ties < 21:
                n = 20
            else:
                n = 21
        else:
            n= Redondeo_int_mas_cerca( ties )
#
# n= 10x + y
#
        y= n % 10# resto de n dividido 10 ==> da el subtipo espectral
        x= (n - y) / 10# da el tipo espectral
#
        if x == 0:# tipo espectral O
            te= "O"
        elif x == 1:# tipo espectral B
            te= "B"
        elif x == 2:# tipo espectral A
            te= "A"
        elif x == 3:# tipo espectral F
            te= "F"
        elif x == 4:# tipo espectral G
            te= "G"
        elif x == 5:# tipo espectral K
            te= "K"
        elif x == 6:# tipo espectral M
            te= "M"
#
        te= te + str(y)
        print(te)
        ties= x * 10 + y
#
        return ties

print(Calculo_te(21.9))