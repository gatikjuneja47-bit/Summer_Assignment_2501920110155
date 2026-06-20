print("Column-wise Sum")
import numpy as np
rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))
matrix = np.array([[int(input(f"Enter element [{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)])

col_sums = np.sum(matrix, axis=0)
print("Column-wise sums:")
for j in range(cols):
    print(f"Sum of column {j + 1}: {col_sums[j]}")