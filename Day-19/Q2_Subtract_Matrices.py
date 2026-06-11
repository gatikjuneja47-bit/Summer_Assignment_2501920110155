print("Subtraction of Matrices")
import numpy as np
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
print("Enter the elements of the first matrix:")
matrix1 = np.array([[int(input(f"Enter element a[{i+1}][{j+1}]: ")) for j in range(col)] for i in range(row)])
print("Enter the elements of the second matrix:")
matrix2 = np.array([[int(input(f"Enter element b[{i+1}][{j+1}]: ")) for j in range(col)] for i in range(row)])
result = matrix1 - matrix2
print("The difference of the matrices is:")
print(result)