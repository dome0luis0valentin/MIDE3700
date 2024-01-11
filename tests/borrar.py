import numpy as np

def fill_spaces_with_letters(matrix):
    # Identificar las curvas y sus valores constantes
    curves = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            value = matrix[i][j]
            if value != 99999:
                if value not in curves:
                    curves[value] = []
                curves[value].append((i, j))

    # Rellenar los espacios entre curvas
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 99999:
                # Encontrar la curva más cercana
                nearest_curve_value = min(curves.keys(), key=lambda x: min(np.linalg.norm(np.array([i, j]) - np.array(coord)) for coord in curves[x]))
                matrix[i][j] = nearest_curve_value

    # Asignar letras a los valores constantes
    letter_mapping = {}
    letter = 'A'
    for value in curves:
        letter_mapping[value] = letter
        letter = chr(ord(letter) + 1)

    # Reemplazar los valores constantes con letras en la matriz
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            value = matrix[i][j]
            if value in letter_mapping:
                matrix[i][j] = letter_mapping[value]

    return matrix

# Ejemplo de uso:
N = 5
matrix = np.full((N, N), 99999, dtype=object)
matrix[0:4, 1:2] = 1
matrix[0:5, 3:4] = 2
print(matrix)

result_matrix = fill_spaces_with_letters(matrix)
print(result_matrix)
