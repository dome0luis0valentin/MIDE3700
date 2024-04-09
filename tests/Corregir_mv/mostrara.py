import numpy as np

dir = "/home/valen/PPS/MIDE3700/tests/Corregir_Matrices/Curvas_Numpy/Mv.npy"

matriz = np.load(dir)
print(matriz)


np.savetxt("/home/valen/PPS/MIDE3700/tests/Corregir_mv/Mv.txt", matriz)
