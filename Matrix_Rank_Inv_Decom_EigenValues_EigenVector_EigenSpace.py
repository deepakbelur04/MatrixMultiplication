import numpy as np
from scipy import linalg
from scipy.linalg import lu
import matplotlib.pyplot as mp
from numpy import array

a = np.array([[0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])


####Finding Rank of the Matrix using Gaussian Elimination####
print(len(a))
x = len(a)
y = len(a[0])
if x == y:
    print("its a square matrix")
else:
    print("its not a square matrix>>Gaussian Elimination Not Possible")
    exit()
pl, u = lu(a, permute_l=True)
print("Gaussian Emimination      "+str(u))

r = np.linalg.matrix_rank(u)
print("Rank of Matrix   "+str(r))

if r == y:
    print("Its a Full Rank Matrix")
else:
    print("Its not a Full Rank Matrix")

#####Finiding Inverse of the Matrix#######

invA = linalg.inv(a)
print("Inverse of the Matrix is\r\n"+str(invA))
#print(invA.dot(a))
#b = a.dot(linalg.inv(a))
#print(b)

#### Finding Determinant of the Matrix########
b = linalg.det(a)
print("Determinant of the Martix"+str(b))

######Finding Eigen Value and Eigen Vector of the Matrix######
la, v = linalg.eig(a)
l1, l2, l3 = la
print("Eigen Value of the Matrix is     ", l1, l2, l3)   # eigenvalues
print("first eigenvector", v[:, 0])
print("second eigenvector", v[:, 1])
print("third eigenvector", v[:, 2])

#fig = mp.figure()
#ax = fig.gca(projection='3d')
#ax.plot(np.linspace(0, v[:, 0]), np.linspace(0, v[:, 1]), np.linspace(0, v[:, 2]))
