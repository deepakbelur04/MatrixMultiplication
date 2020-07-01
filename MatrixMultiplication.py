
# Program to multiply two matrices (vectorized implementation)
import numpy as np

# take a 3x3 matrix
A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

# take a 3x3 matrix
B = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

# result will be 3x3

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

result = np.dot(A, B)

for r in result:
    print(r)