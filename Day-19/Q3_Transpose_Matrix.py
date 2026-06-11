print("Transpose of a Matrix")
import numpy as np
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
print("Enter the elements of the matrix:")
matrix = np.array([[int(input(f"Enter element [{i+1}][{j+1}]: ")) for j in range(col)] for i in range(row)])
print("The original matrix is: ")
print(matrix)
transpose = np.array([], dtype=int)
for j in range(col):
    for i in range(row):
        transpose = np.append(transpose, matrix[i][j])
print("The transpose of the matrix is: ")
print(transpose.reshape(col, row))