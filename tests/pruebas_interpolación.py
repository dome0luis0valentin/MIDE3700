from random import randint
import matplotlib.pyplot as plt

def probar(curvas):
    # x: 0.19 - 0.22
    # y: 43.0 - 84.0

    # Resultados esperados:
    # 0.20291153295793762, 47.699999999999996 
    # 8.587815329576427e-05
    # 0.20291153295793762, 57.699999999999996 
    # 0.00020111115329582503
    # 0.20291153295793762, 67.69999999999999 
    # 0.03678649115329574
    # 0.20291153295793762, 70.0 
    # 0.05978649115329585
    # 0.20291153295793762, 72.0 
    # 0.07978649115329585
    # 0.2092871629443298, 48.79468500005078 
    # 0.0002956857168022114
    
    #Casos fijos:
    xs = [0.20291153295793762, 0.20291153295793762, 0.20291153295793762, 0.20291153295793762, 0.20291153295793762]
    ys = [4.77, 5.77, 6.77, 7.00, 7.20]
    # xs = [0.20291153295793762, 0.20291153295793762, 0.20291153295793762, 0.20291153295793762, 0.20291153295793762]
    # ys = [5.77, 6.77, 7.77, 8.77, 9.77]
    
    magnitudes = []
    ejex = []
    ejey = []
    
    for x,y in zip(xs,ys):

    # for i in range(4300, 8400, 100):
    # if (True):
        # x = float(randint(1900, 2200)/10000)
        # y = float(randint(4300, 8400)/100)
        # y = i / 100
        y *= 10
        print(f"Prueba con {x , y}")
        ejex.append(x)
        ejey.append(y)
        a, b, c = curvas.Interpolo(x, y)

        magnitudes.append(b)

    plt.scatter(ejex, ejey, color="red", marker=".")
    # print(f"Esta son la lista de magnitudes: ", magnitudes)
    # for i in magnitudes:
    #     print(i)