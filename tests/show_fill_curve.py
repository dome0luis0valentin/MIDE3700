import glob
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('TkAgg')

# Lists to store the x and y coordinates

# Get a list of all .dat files in the directory
try:
    dir = sys.argv[1]
except IndexError:
    dir = 'Teff'
finally:
    print("No argument given, using Teff as default")

file_list = glob.glob(f'/home/valen/PPS/MIDE3700/tests/Curvas_Densas/{dir}/*.dat')


# file_list = glob.glob(f'/home/valen/pps/MIDE3700_v2/MIDE3700/Curvas/{dir}/*.dat')

x_values = []
y_values = []
cant_files = len(file_list)
print("Cantidad de archivos: ",cant_files)
list_curves = []
x_values = []
y_values = []
# Iterate over the files
valores = []

print("Leyendo archivos...")
for file_path in file_list:
    # Open the file and read the coordinates
    with open(file_path, 'r') as f:
        
        for line in f:
            if line.startswith("#"):
                # valores.append(line.split()[5])
                continue
            else:
                x, y = map(float, line.strip().split())
                x_values.append(x)
                y_values.append(y)
                
    # Create a scatter plot
plt.scatter(x_values, y_values, color='blue', marker='.')
print(len(x_values))
print("fin de lectura")

# Set axis labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
print(file_list)
plt.title(file_list[0].split('/')[-1].split('.')[0])


# Show the plot
plt.show()