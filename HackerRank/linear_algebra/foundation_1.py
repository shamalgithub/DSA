import numpy as np
from numpy.linalg import matrix_power 
# Define the matrices
A = np.array([[1, 2, 3],
              [2, 3, 4],
              [1, 1, 1]])

B = np.array([[4, 5, 6],
              [7, 8, 9],
              [4, 5, 7]])

c = np.array([[-2 , -9],[1 , 4]])
print((A*B))
print(matrix_power(c , 1000))