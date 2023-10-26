#import MIDE3700 as app
import cProfile
import subprocess

def fun():

# Ruta al archivo a ejecutar (puedes ajustar la ruta según sea necesario)
    archivo_a_ejecutar = 'MIDE3700.py'
    print("Ejec")

# Ejecuta el archivo
    subprocess.call(['python3', archivo_a_ejecutar])

    return 
if __name__ == '__main__':
    #fun()
    print("Ejec")
    cProfile.run('fun()')

