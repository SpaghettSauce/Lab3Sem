import numpy as np

def calculate_matrix(mat):
    sum_elements = np.sum(mat)
    max_matrix_value = np.max(mat)
    min_matrix_value = np.min(mat)
    return sum_elements, max_matrix_value, min_matrix_value




matrix = np.genfromtxt('matrix.txt', delimiter=',')
print("Matrix: ")
print(matrix)

print("")
print(calculate_matrix(matrix))