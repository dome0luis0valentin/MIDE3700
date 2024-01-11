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

file_list = glob.glob(f'/home/valen/pps/MIDE3700_v2/MIDE3700/Curvas/{dir}/*.dat')
x_values = []
y_values = []
cant_files = len(file_list)
print(cant_files)
list_curves = []
x_values = []
y_values = []
# Iterate over the files
for file_path in file_list:
    # Open the file and read the coordinates
    with open(file_path, 'r') as f:
        
        for line in f:
            if line.startswith("#"):
                continue
            else:
                x, y = map(float, line.strip().split())
                x_values.append(x)
                y_values.append(y)
                
    # Create a scatter plot
plt.scatter(x_values, y_values, color='blue', marker='.')


# Add color between curve 0 and curve 1
if len(list_curves) >= 2:
    plt.fill_between(x_values, y_values, list_curves[1].get_offsets()[:, 1], color='gray')

# Set axis labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of Data')

# Show the plot
plt.show()
