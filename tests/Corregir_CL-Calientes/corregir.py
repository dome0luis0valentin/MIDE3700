"""
    La idea de este programa es tomar la matriz que ya esta coloreada, y terminar de colorear la sección que aún no lo esta
    entre las curvas 0.0 y 1.0, para esto
    Tomo la matriz cargada en Numpy, y desde el punto (0,29) hasta el punto (117,70) de la matriz
    trazo una linea imaginaria, que a partir de ella para arriba se debe colorear con el valor 0.0
"""
dir = "/home/valen/PPS/MIDE3700/tests/Curvas_Numpy/CL-Calientes.npy"

import numpy as np
import matplotlib.pyplot as plt

m = np.load(dir)

def recta(x):
    return (-0.3504 * x - 29) * -1
x = 0

for x in range(0,118):
    y = recta(x)
   
    try:
        m[int(y), int(x)] = 0.0
        for i in range(int(x), int(x)+160):
            if (m[int(y),i ] == 1.0):
                break
            m[int(y),i ] = 0.0
        # plt.imshow(m, cmap='hot', interpolation='nearest')
        # plt.show()
    except:
        print("Error en el punto", x, y)

np.save("./CL-Calientes.npy", m)
np.savetxt("./CL-Calientes.txt", m)
# plt.imshow(m, cmap='hot', interpolation='nearest')
# plt.show()


