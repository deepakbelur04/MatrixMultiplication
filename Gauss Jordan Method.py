import numpy as np
import numpy.linalg as la
import timeit
import unittest
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import copy

############################################################
# Problem 1: Gauss-Jordan Elimination
############################################################

def gauss_jordan(A):
    A_original = copy.deepcopy(A)
    A = A.astype(float)
    #i_star_array = []
    B = []
    for k in range(A.shape[0]):
        for i in range(k, A.shape[0]):
            #i_star_array.append(np.argmax(np.abs(A[i][k]), axis=0))
            i_star = np.argmax(np.abs(A[i][k]), axis=0)

            if A[i_star][k] == 0:
                B.append(0)

            tmp = k
            A[k, :] = A[i_star, :]
            A[i_star, :] = A[tmp, :]

        for j in range(k + 1, A.shape[0]):

            f = A[j][k] / A[k][k]
            A[j, :] = A[j, :] - f * A[k, :]



    for k in range(A.shape[0] - 1, -1, -1):
        A[k, :] = A[k, :] / A[k, k]
        for j in range(k - 1, -1, -1):
            f = A[j][k] / A[k][k]
            A[j, :] = A[j, :] - f * A[k, :]

    if all(v == 0 for v in B):
        print("Matrix is not invertible")
        return A
    else:
        return A

Ar = np.array([[1, 2, -1, 0], [3, 1, -1, 0], [-1, -1, 2, 2], [3, 2, -1, 2]],dtype=float)
print(gauss_jordan(Ar))
