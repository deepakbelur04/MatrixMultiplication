matrixA = [[1, 4, 3],
           [5, 7, 9],
           [2, 7, 8]]

matrixB = [[4, 3, 2],
           [7, 1, 5],
           [2, 9, 1]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

zipMatrix = zip(matrixA, matrixB)
tupleZipMatrix = tuple(zipMatrix)

print(tupleZipMatrix[0][0][2])

columnLenA = int(len(matrixA))
rowLenA = int(len(matrixA[0]))

columnLenB = int(len(matrixB))
rowLenB = int(len(matrixB[0]))


def dotProduct(sampleMatrix1, sampleMatrix2):
    for i in range(rowLenA):
        for j in range(columnLenB):
            for k in range(rowLenA):
                result[i][j] += sampleMatrix1[i][k] * sampleMatrix2[k][j]
    print(result)


def columnProduct(sampleMatrix1, sampleMatrix2):
    for i in range(columnLenB):
        for j in range(columnLenA):
            for k in range(columnLenB):
                result[i][j] += sampleMatrix2[k][i] * sampleMatrix1[k][j]
    print(result)


def rowProduct(sampleMatrix1, sampleMatrix2):
    for i in range(rowLenA):
        for j in range(columnLenB):
            total = 0
            for ii in range(columnLenA):
                total += sampleMatrix1[i][ii] * sampleMatrix2[ii][j]
            result[i][j] = total
    print(result)



def outerProduct(sampleMatrix1, sampleMatrix2):
    print('Dekhiba3')


def blockProduct(sampleMatrix1, sampleMatrix2):
    print('Dekhiba4')


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
      "5. Block Multiplication\n")
optionNumber = int(input("Choose a value above from 1 to 5\n"))

print(optionNumber)

if optionNumber == 1:
    print("you have selected a dot product multiplication")
    dotProduct(matrixA, matrixB)

elif optionNumber == 2:
    print("you have selected a Column method multiplication")
    columnProduct(matrixA, matrixB)

elif optionNumber == 3:
    print("you have selected a Row method multiplication")
    rowProduct(matrixA, matrixB)
elif optionNumber == 4:
    print("you have selected a Outer Product multiplication")
    outerProduct(matrixA, matrixB)
elif optionNumber == 5:
    print("you have selected a Block multiplication")
    blockProduct(matrixA, matrixB)
else:
    print("Invalid Entry or Choice")