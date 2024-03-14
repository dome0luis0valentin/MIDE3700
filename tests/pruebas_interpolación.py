from random import randint
import matplotlib.pyplot as plt

def probar(curvas):
    # x: 0.19 - 0.22
    # y: 43.0 - 84.0

    # Resultados esperados:
    # 11439.17427135962
    # 11526.617961425418
    # 11621.862838432991
    # 11621.862838432991
    # 11720.89565222022
    
    #Casos fijos:
    xs = [0.20291153295793762, 0.20291153295793762, 0.20291153295793762, 0.20291153295793762, 0.20291153295793762]
    ys = [4.77, 5.77, 6.77, 7.77, 8.77]
    
    magnitudes = []
    ejex = []
    ejey = []
    
    for x,y in zip(xs,ys):

    # for i in range(4300, 8400, 100):
    # if (True):
        # x = float(randint(1900, 2200)/10000)
        # y = float(randint(4300, 8400)/100)
        # y = i / 100

        print(f"Prueba con {x , y}")
        ejex.append(x)
        ejey.append(y)
        a, b, c = curvas.Interpolo(x, y)

        magnitudes.append(b)

    plt.scatter(ejex, ejey, color="red", marker=".")
    print(f"Esta son la lista de magnitudes: ", magnitudes)
    for i in magnitudes:
        print(i)