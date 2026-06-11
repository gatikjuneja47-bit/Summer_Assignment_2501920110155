print("Input and Display of an Array")
import numpy as np
n = int(input("Enter the number of elements in the array: "))
arr=np.array([int(input(f"Enter element {i+1}: ")) for i in range(n)])
print("Array: " ,arr)