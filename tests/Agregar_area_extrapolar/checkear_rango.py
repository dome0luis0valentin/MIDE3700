import glob

max_x = -10000
max_y = -10000
min_x = 10000
min_y = 10000

def evaluar_dir(curvas):
    """
    
    """
    superiores = f"/home/valen/PPS/MIDE3700/tests/Agregar_area_extrapolar/output_relleno_fino_superiores/{curvas}*.dat"
    inferiores = f"/home/valen/PPS/MIDE3700/tests/Agregar_area_extrapolar/output_relleno_fino_inferiores/{curvas}*.dat"

    arch_inf = glob.glob(inferiores)

    archs = glob.glob(superiores)
    archs.extend(arch_inf)
    global max_x
    global max_y
    global min_x
    global min_y
    
    
    for arch in archs:
        with open(arch, 'r') as f:
            for line in f:
                if line.startswith("#"):
                    continue
                else:
                    x = float(line.strip().split()[0])
                    y = float(line.strip().split()[1])
                    
                    if x > max_x:
                        max_x = x
                    if y > max_y:
                        max_y = y

                    if x < min_x:
                        min_x = x
                    if y < min_y:
                        min_y = y


    print(f"Para la curva {curvas}:\n min_x: {round(min_x)}\n max_x {max_x}\n min_y {min_y}\n max_y {max_y}")
lista_input = ["Logg/", "Mbol/", "PHIo/Frias/", "PHIo/Calientes/", "TE/Frias/", "TE/Calientes/", "Mv/", "Teff/"]

for curvas in lista_input:
    evaluar_dir(curvas)