dir_curvas = "/home/valen/PPS/MIDE3700/tests/Rellenar_curvas_v2/input_matrices_con_curvas/"
dir_matrices_map = "/home/valen/PPS/MIDE3700/tests/Rellenar_curvas_v2/output_nuevas_curvas_np"

import os
import numpy as np

def superponer(m1, m2):
    print(m1.shape, m2.shape)
    for i in range(m1.shape[0]):
        for j in range(m1.shape[1]):
            if m1[i,j] != 99999.0:
                m2[i,j] = m1[i,j]
    return m2

curvas = os.listdir(dir_curvas)
matrices_map = os.listdir(dir_matrices_map)

for curva in curvas:
    name_curve = curva.split(".")[0]
    for matriz in matrices_map:
        name_matriz = matriz.split(".")[0]

        if name_curve == name_matriz:
            dir = dir_curvas+"/"+curva
            m1 = np.load(dir)
            print(dir)
            dir2 = dir_matrices_map+"/"+matriz
            print(dir2)
            m2 = np.load(dir2, allow_pickle=True)

            m_res = superponer(m1, m2)
            # np.savetxt("resultado_en_text/"+name_curve+".npy", m_res, fmt="%-10s", delimiter="|")
            np.save("resultado/"+name_curve+".npy", m_res)
