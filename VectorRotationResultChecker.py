import numpy as np
import matplotlib as mpl

matrixY = [[np.cos(45), 0, -np.sin(45)],
           [0, 1, 0],
           [np.sin(45), 0, np.cos(45)]]

matrixZ = [[np.cos(45), -np.sin(45), 0],
           [np.sin(45), np.cos(45), 0],
           [0, 0, 1]]

matrixX = [[1, 0, 0],
           [0, np.cos(45), -np.sin(45)],
           [0, np.sin(45), np.cos(45)]]

matrixB = [[9],
           [0],
           [9]]

result = [[0],
          [0],
          [0]]


def dotProduct(sampleMatrix1, sampleMatrix2):
    # for i in range(rowLenA):
    #     for j in range(columnLenB):
    #         for k in range(rowLenA):
    #             result[i][j] += sampleMatrix1[i][k] * sampleMatrix2[k][j]
    # print(result)
    # x= np.array(sampleMatrix1)
    # y= np.array(sampleMatrix2)
    z = np.dot(sampleMatrix1, sampleMatrix2)
    # np.reshape(z,(3,3))
    print("XZ Plane" +str(z))

    z = np.dot(matrixZ, z)
    # np.reshape(z,(3,3))
    print("XY Plane" +str(z))

    z = np.dot(matrixZ, z)
    # np.reshape(z,(3,3))
    print("XY Plane" +str(z))

    z = np.dot(matrixX, z)
    # np.reshape(z,(3,3))
    print("YZ Plane" + str(z))

dotProduct(matrixY, matrixB)
