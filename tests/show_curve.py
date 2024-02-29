import glob
import matplotlib.pyplot as plt
import sys

# Lists to store the x and y coordinates

# Get a list of all .dat files in the directory
try:
    dir = sys.argv[1]
except IndexError:
    dir = 'Teff'
finally:
    print("No argument given, using Teff as default")

#file_list = glob.glob(f'/home/valen/PPS/MIDE3700/tests/Curvas_Densas/{dir}/*.dat')

file_list = glob.glob(f'/home/valen/PPS/MIDE3700/tests/output_relleno_fino/Mv/*.dat')
    
# file_list = glob.glob(f'/home/valen/pps/MIDE3700_v2/MIDE3700/Curvas/{dir}/*.dat')

x_values = []
y_values = []
cant_files = len(file_list)
print(cant_files)
list_curves = []
x_values = []
y_values = []
# Iterate over the files
valores = []
for file_path in file_list:
    # Open the file and read the coordinates
    with open(file_path, 'r') as f:
        
        for line in f:
            if line.startswith("#"):
                valores.append(line.split()[5])
                continue
            else:
                x, y = map(float, line.strip().split())
                x_values.append(x)
                y_values.append(y)
                
    # Create a scatter plot
plt.scatter(x_values, y_values, color='blue', marker='.')
print(len(x_values))

# Add color between curve 0 and curve 1
if len(list_curves) >= 2:
    plt.fill_between(x_values, y_values, list_curves[1].get_offsets()[:, 1], color='gray')

# Set axis labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
print(file_list)
plt.title(file_list[0].split('/')[-1].split('.')[0])

print(valores)
valores.sort()


for i in range(0, len(valores)-1):
    print('"'+valores[i]+f'" : ({valores[i]} ,{valores[i-1]} ),')

print('"'+valores[i]+f'" : (None , None ')
# Show the plot
plt.show()
