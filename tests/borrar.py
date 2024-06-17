import numpy as np
from matplotlib import pyplot as plt
import os
import math

def distancia_euclidea_v2(x1, x2, y1, y2):
    di = ((x1 - x2) ** 2)
    dj = ((y1 - y2) ** 2)
    
    return math.sqrt( di + dj )

if __name__ == "__main__":
    args = os.sys.argv
    x1 = float(args[1])
    x2 = float(args[2])
    y1 = float(args[3])
    y2 = float(args[4])
    print(distancia_euclidea_v2(x1, x2, y1, y2))



# input = "./Mapear_Curvas_Externas/output_txt/TE-Calientes.txt"
# input2 = "./Mapear_Curvas_Externas/output/TE-Calientes.npy"

# # m_np = np.load(input2, allow_pickle=True)

# # print(m_np)
# # np.savetxt("./Mapear_Curvas_Externas/output_txt/TE-Calientes-Copy.txt", m_np, fmt='%s', delimiter='|')
# #vuelvo a cargar la matriz que guarde como texto
# m_txt = np.loadtxt("./Mapear_Curvas_Externas/output_txt/TE-Calientes-Copy.txt", delimiter='|', dtype=object)
# # print(m_txt)

# # print(m_np == m_txt)

# np.save("./Mapear_Curvas_Externas/output/TE-Calientes-Copy.npy", m_txt)


# # m1 = np.load(input)
# # m2 = np.load(input2)

# # plt.imshow(m1, cmap='viridis', interpolation='nearest', origin='upper')
# # #Reemplaza los valores de la matriz en 99999.0 por 1
# # for i in range(m2.shape[0]):
# #     for j in range(m2.shape[1]):
# #         if m2[i][j] == 99999.0:
# #             m2[i][j] = 1

# # ax, fig = plt.subplots()
# # plt.imshow(m2, cmap='viridis', interpolation='nearest', origin='upper')
# # print(m1.shape, m2.shape)
# # plt.show()