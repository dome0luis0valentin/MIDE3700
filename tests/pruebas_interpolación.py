from random import randint
import matplotlib.pyplot as plt


def probar_errores(curvas):

   #Casos fijos:
    xs = [x/1000 for x in range(150, 600, 30)]
    ys = [y for y in range(10, 80, 5)]
    #0.21, 20), (0.24, 10), (0.24, 15), (0.27, 10), (0.3, 10), (0.39, 60), (0.39, 65), (0.42, 55), (0.42, 60), (0.42, 65), (0.42, 70), (0.45, 55), (0.45, 70), (0.48, 50), (0.48, 55), (0.48, 70), (0.48, 75), (0.51, 50), (0.51, 75), (0.54, 50), (0.57, 45), (0.57, 50)]
    casos = [(0.15, 25), (0.15, 30), (0.18, 20), (0.18, 25), (0.21, 15)]
    errores = []
    magnitudes = []

    for c in casos:
        x = c[0]
        y = c[1]
        print(f"Prueba con {x , y}")
        m = curvas.Interpolo(x, y)[1]
        error = curvas.Error(x,y,m)
        print(f"Error: {error}")
        errores.append(error)
        magnitudes.append(m)
   
    # print(f"Entrada: \nxs = {xs}\nys = {ys}")
    print("Magnitudes: ", magnitudes)
    print("Entrada: ", casos)
    print(f"Errores = ", errores)

def probar_mv(curvas):
    # x: 0.19 - 0.22
    # y: 43.0 - 84.0

    #Casos fijos:
    # xs = [x/1000 for x in range(50, 500, 40)]
    # ys = [y for y in range(-10, 75,20)]

    # xs = [0.09]
    # ys = [70]
    
    # xs = [0.20291153295793762, 0.20291153295793762, 0.20291153295793762, 0.20291153295793762, 0.20291153295793762]
    # ys = [5.77, 6.77, 7.77, 8.77, 9.77]

    # xs = [x/1000 for x in range(150, 600, 20)]
    # ys = [y for y in range(10, 80, 5)]
    xs = [0.17, 0.19, 0.21, 0.21]
    ys = [65, 65, 65, 75]

    magnitudes = []
    ejex = []
    ejey = []
    
    # for x,y in zip(xs,ys):
    for x, y in zip(xs, ys):
        # for y in ys:

    # for i in range(4300, 8400, 100):
        if (True):
        # x = float(randint(1900, 2200)/10000)
        # y = float(randint(4300, 8400)/100)
        # y = i / 100
            # y *= 10
            y = round(y, 2)
            print(f"Prueba con {x , y}")
            ejex.append(x)
            ejey.append(y)
            a, b, c = curvas.Interpolo(x, y)

            magnitudes.append(b)
            #redondear cada valor de la lista ejey a 2 decimales con una función lambda

    # valores = [19375.0, 19375.0, 19375.0, 19882.20742392061, 19375.0, 19062.5, 19062.5, 19062.5, 19826.834984182427, 19062.5, 18750.0, 18750.0, 18750.0, 19773.753109471978, 18750.0, 18437.5, 18437.5, 18437.5, 19722.913965907013, 18437.5, 18750.0, 18750.0, 18750.0, 19773.753109471978, 18750.0]
    # plt.scatter(ejex, ejey, color="red", marker=".")
    # plt.show()
    print("casos de entrada: ", ejex, ejey)
    print(f"Esta son la lista de magnitudes: ", magnitudes)
    # for a, b, c, d in zip(ejex, ejey, magnitudes, valores):
    #     print(a, b, c-d)
    for i in magnitudes: 
        print(i)

    # plt.show()

def probar(curvas):
    # x: 0.19 - 0.22
    # y: 43.0 - 84.0

    #Casos fijos:
    xs = [x/1000 for x in range(50, 500, 40)]
    ys = [y for y in range(-10, 75,20)]

    # xs = [0.09]
    # ys = [70]
    
    xs = [0.20291153295793762, 0.20291153295793762, 0.20291153295793762, 0.20291153295793762, 0.20291153295793762]
    ys = [5.77, 6.77, 7.77, 8.77, 9.77]
    
    magnitudes = []
    ejex = []
    ejey = []
    
    # for x,y in zip(xs,ys):
    for x in xs:
        for y in ys:

    # for i in range(4300, 8400, 100):
    # if (True):
        # x = float(randint(1900, 2200)/10000)
        # y = float(randint(4300, 8400)/100)
        # y = i / 100
            y *= 10
            y = round(y, 2)
            print(f"Prueba con {x , y}")
            ejex.append(x)
            ejey.append(y)
            a, b, c = curvas.Interpolo(x, y)

            magnitudes.append(b)
            #redondear cada valor de la lista ejey a 2 decimales con una función lambda

    # valores = [19375.0, 19375.0, 19375.0, 19882.20742392061, 19375.0, 19062.5, 19062.5, 19062.5, 19826.834984182427, 19062.5, 18750.0, 18750.0, 18750.0, 19773.753109471978, 18750.0, 18437.5, 18437.5, 18437.5, 19722.913965907013, 18437.5, 18750.0, 18750.0, 18750.0, 19773.753109471978, 18750.0]
    # plt.scatter(ejex, ejey, color="red", marker=".")
    print(f"Esta son la lista de magnitudes: ", magnitudes)
    # for a, b, c, d in zip(ejex, ejey, magnitudes, valores):
    #     print(a, b, c-d)
    for i in magnitudes: 
        print(i)

    # plt.show()


def comprobar():
    m1 = [99999.0, 16666.666666666668, 22500.0, 36666.666666666664, 35478.9131426106, 99999.0, 14642.857142857143, 19642.85714285714, 27500.0, 36436.7394278318, 99999.0, 13214.285714285714, 18214.285714285714, 23750.0, 23074.718121287027, 99999.0, 12250.0, 16785.714285714286, 22344.074484684745, 21666.666666666668, 99999.0, 11750.0, 15357.142857142857, 17655.925515315255, 18750.0, 99999.0, 11250.0, 14166.666666666666, 16500.0, 16250.0, 99999.0, 10777.777777777777, 13055.555555555557, 14687.500000000002, 14166.666666666668, 99999.0, 10333.333333333334, 12166.666666666666, 13437.5, 12500.0, 99999.0, 9875.0, 11500.0, 12312.5, 12093.78022314386, 99999.0, 9375.0, 10888.888888888889, 11562.5, 10333.333333333334, 99999.0, 8875.0, 10444.444444444445, 10800.0, 10084.959387950164, 99999.0, 8375.000000000002, 10000.0, 10000.0, 9884.615384615385]
    m2 = [99999.0, 16666.666666666668, 22500.0, 99999.0, 99999.0, 99999.0, 14642.857142857143, 19642.85714285714, 27500.0, 30000.0, 99999.0, 13214.285714285714, 18214.285714285714, 23750.0, 26000.0, 99999.0, 12250.0, 16785.714285714286, 21250.0, 21666.666666666668, 99999.0, 11750.0, 15357.142857142857, 18750.0, 18750.0, 99999.0, 11250.0, 14166.666666666666, 16500.0, 16250.0, 99999.0, 10777.777777777777, 13055.555555555555, 14687.5, 14166.666666666666, 99999.0, 10333.333333333334, 12166.666666666666, 13437.5, 12500.0, 99999.0, 9875.0, 11500.0, 12312.5, 11750.0, 99999.0, 99999.0, 10888.888888888889, 11562.5, 11000.0, 99999.0, 99999.0, 10444.444444444445, 10800.0, 10200.0, 99999.0, 99999.0, 10000.0, 10000.0, 99999.0]

    ejes = [(0.05, -10), (0.05, 10), (0.05, 30), (0.05, 50), (0.05, 70), (0.09, -10), (0.09, 10), (0.09, 30), (0.09, 50), (0.09, 70), (0.13, -10), (0.13, 10), (0.13, 30), (0.13, 50), (0.13, 70), (0.17, -10), (0.17, 10), (0.17, 30), (0.17, 50), (0.17, 70), (0.21, -10), (0.21, 10), (0.21, 30), (0.21, 50), (0.21, 70), (0.25, -10), (0.25, 10), (0.25, 30), (0.25, 50), (0.25, 70), (0.29, -10), (0.29, 10), (0.29, 30), (0.29, 50), (0.29, 70), (0.33, -10), (0.33, 10), (0.33, 30), (0.33, 50), (0.33, 70), (0.37, -10), (0.37, 10), (0.37, 30), (0.37, 50), (0.37, 70), (0.41, -10), (0.41, 10), (0.41, 30), (0.41, 50), (0.41, 70), (0.45, -10), (0.45, 10), (0.45, 30), (0.45, 50), (0.45, 70), (0.49, -10), (0.49, 10), (0.49, 30), (0.49, 50), (0.49, 70)]

    for i, j, k in zip(ejes, m1, m2):
        print("Caso", i)
        if (j-k) > 0 :
            print("Dif: ", str(round(abs(j-k), 5)).rjust(5, " "), str(j).rjust(20, "*")," - ", k)
comprobar()