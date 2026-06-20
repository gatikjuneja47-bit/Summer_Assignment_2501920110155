print("Row-wise Sum")
import numpy as np
rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))
matrix = np.array([[int(input(f"Enter element [{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)])

row_sums = np.sum(matrix, axis=1)
print("Row-wise sums:")
for i in range(rows):
    print(f"Sum of row {i+1}: {row_sums[i]}")