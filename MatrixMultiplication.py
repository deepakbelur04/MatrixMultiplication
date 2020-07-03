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

zipMatrix = zip(matrixY, matrixB)
tupleZipMatrix = tuple(zipMatrix)

#print(tupleZipMatrix[0][0][2])

columnLenA = int(len(matrixY))
rowLenA = int(len(matrixY[0]))

columnLenB = int(len(matrixB))
rowLenB = int(len(matrixB[0]))


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



def columnProduct(sampleMatrix1, sampleMatrix2):
    # for i in range(rowLenA):
    #     for j in range(columnLenB):
    #         for k in range(rowLenA):
    #             result[i][j] += sampleMatrix2[k][i] * sampleMatrix1[k][j]
    x = np.array(sampleMatrix1)
    y = np.array(sampleMatrix2)
    z = x @ y
    result = np.array(z)
    np.reshape(result, (3, 3))
    print(result)


def rowProduct(sampleMatrix1, sampleMatrix2):
    # for i in range(rowLenA):
    #     for j in range(columnLenB):
    #         for k in range(columnLenA):
    #             result[i][j] += sampleMatrix1[i][k] * sampleMatrix2[k][j]
    # print(result)
    x = np.array(sampleMatrix1)
    y = np.array(sampleMatrix2)
    z = np.matmul(x, y)
    print(z)


def outerProduct(sampleMatrix1, sampleMatrix2):
    x = np.array(sampleMatrix1)
    y = np.array(sampleMatrix2)

    z = [[0,0,0],
        [0,0,0],
        [0,0,0]]
    for j in range(len(x)):
        matrix_temp_1 = x[:, j:j + 1]
        matrix_temp_2 = y[j:j + 1, :]
        # print (matrix_temp_1)
        # print(matrix_temp_2)
        num = np.dot(matrix_temp_1, matrix_temp_2)
        # print(num)
        z += num

    print(z)


def blockProduct(sampleMatrix1, sampleMatrix2):
    #x = np.array(sampleMatrix1)
    #y = np.array(sampleMatrix2)
    print("Team has doubt about Block Multiplication of Symentric Matrix hence this has not been completed")


# Comparing the Column length of A with Row Length of B matrix

if (rowLenA == columnLenB):
    print("Multiplication is possible")
else:
    print("Matrix multiplication is not Possible")

print("what type of multiplication would you like to do for matrixA and matrixB ?")

print("1. Dot Product\n"
      "2. Column Method\n"
      "3. Row Method\n"
      "4. Outer Product\n"
      "5. Block Multiplication")
optionNumber = int(input("Choose a value above from 1 to 5\n"))

print(optionNumber)

if optionNumber == 1:
    print("you have selected a dot product multiplication")
    dotProduct(matrixY, matrixB)

elif optionNumber == 2:
    print("you have selected a Column method multiplication")
    columnProduct(matrixY, matrixB)

elif optionNumber == 3:
    print("you have selected a Row method multiplication")
    rowProduct(matrixY, matrixB)
elif optionNumber == 4:
    print("you have selected a Outer Product multiplication")
    outerProduct(matrixY, matrixB)
elif optionNumber == 5:
    print("you have selected a Block multiplication")
    blockProduct(matrixY, matrixB)
else:
    print("Invalid Entry or Choice")