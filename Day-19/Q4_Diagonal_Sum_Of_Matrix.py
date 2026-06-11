print("Diagonal Sum of a Matrix")
import numpy as np 
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
print("Enter the elements of the matrix:")
matrix = np.array([[int(input(f"Enter element [{i+1}][{j+1}]: ")) for j in range(col)] for i in range(row)])
print("The original matrix is: ")
print(matrix)
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(min(row, col)):
    primary_diagonal_sum += matrix[i][i]

for i in range(min(row, col)):
    secondary_diagonal_sum += matrix[i][col - 1 - i]

print(f"The sum of the primary diagonal is: {primary_diagonal_sum}")
print(f"The sum of the secondary diagonal is: {secondary_diagonal_sum}")