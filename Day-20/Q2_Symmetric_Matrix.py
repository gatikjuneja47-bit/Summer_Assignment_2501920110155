print("Symmetric Matrix")
import numpy as np
rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))
if rows != cols:
    print("Error")
else:
    matrix = np.array([[int(input(f"Enter element [{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)])
    is_symmetric = True
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                is_symmetric = False
                break
        if not is_symmetric:
            break
    if is_symmetric:
        print("The matrix is symmetric.")
    else:
        print("The matrix is not symmetric.")