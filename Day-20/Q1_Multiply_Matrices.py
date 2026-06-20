print("Multiply Matrices")
import numpy as np
row1 = int(input("Enter the number of rows for the first matrix: "))
col1 = int(input("Enter the number of columns for the first matrix: "))
row2 = int(input("Enter the number of rows for the second matrix: "))
col2 = int(input("Enter the number of columns for the second matrix: "))
if col1 != row2:
    print("Error")
else:
    matrix1 = np.array([[int(input(f"Enter element [{i+1}][{j+1}] of the first matrix: ")) for j in range(col1)] for i in range(row1)])
    matrix2 = np.array([[int(input(f"Enter element [{i+1}][{j+1}] of the second matrix: ")) for j in range(col2)] for i in range(row2)])
    result = np.array([], dtype=int)
    for i in range(row1):
        for j in range(col2):
            sum = 0
            for k in range(col1):
                sum += matrix1[i][k] * matrix2[k][j]
            result = np.append(result, sum)
    result = result.reshape(row1, col2)
    print(f"Result: {result}")