from random import randint
import matplotlib.pyplot as plt

def probar(curvas):
    # x: 0.19 - 0.22
    # y: 43.0 - 84.0

    #Casos fijos:
    xs = [0.20, 0.205, 0.21, 0.215, 0.21]
    ys = [4.77, 5.2, 5.77, 6.3, 6.77]
    ys = sorted(ys)
    # xs = [0.20291153295793762, 0.20291153295793762, 0.20291153295793762, 0.20291153295793762, 0.20291153295793762]
    # ys = [5.77, 6.77, 7.77, 8.77, 9.77]
    
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

    valores = [19375.0, 19375.0, 19375.0, 19882.20742392061, 19375.0, 19062.5, 19062.5, 19062.5, 19826.834984182427, 19062.5, 18750.0, 18750.0, 18750.0, 19773.753109471978, 18750.0, 18437.5, 18437.5, 18437.5, 19722.913965907013, 18437.5, 18750.0, 18750.0, 18750.0, 19773.753109471978, 18750.0]
    plt.scatter(ejex, ejey, color="red", marker=".")
    print(f"Esta son la lista de magnitudes: ", magnitudes)
    for a, b, c, d in zip(ejex, ejey, magnitudes, valores):
        print(a, b, c-d)