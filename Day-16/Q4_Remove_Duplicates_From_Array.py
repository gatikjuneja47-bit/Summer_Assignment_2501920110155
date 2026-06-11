print("Remove duplicates from array")
import numpy as np
n = int(input("enter the size of array: "))
arr = np.array([int(input(f"enter element {i+1}: ")) for i in range(n)])
unique_elements = np.unique(arr)
print("array after removing duplicates is:", unique_elements)