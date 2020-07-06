from numpy import array
import numpy as np
from scipy.linalg import lu
a = array([[2, 2, 1, 7], [-1, 2, 0, 3], [3, 2, 1, 8], [4, 2, 0, 8]])
print(len(a))

x = len(a)
y = len(a[0])

if x == y:
    print("its a square matrix")
else:
    print("its not a square matrix>>Gaussian Elimination Not Possible")
    exit()

pl, u = lu(a, permute_l=True)

print(u)

r = np.linalg.matrix_rank(u)
print("Rank of Matrix"+str(r))

if r == y:
    print("Its a Full Rank Matrix")
else:
    print("Its not a Full Rank Matrix")