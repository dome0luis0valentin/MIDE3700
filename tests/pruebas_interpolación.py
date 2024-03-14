from random import randint
import matplotlib.pyplot as plt

def probar(curvas):
    # x: 0.19 - 0.22
    # y: 43.0 - 84.0
    magnitudes = []
    ejex = []
    ejey = []

    for i in range(4300, 8400, 100):
    # if (True):
        x = float(randint(1900, 2200)/10000)
        y = float(randint(4300, 8400)/100)
        y = i / 100
        print(f"Prueba con {x , y}")
        ejex.append(x)
        ejey.append(y)
        a, b, c = curvas.Interpolo(x, y)

        magnitudes.append(b)

    plt.scatter(ejex, ejey, color="red", marker=".")
    print(f"Esta son la lista de magnitudes: ", b)