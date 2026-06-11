print("Linear Search")
import numpy as np
n = int(input("Enter the number of elements in the array: "))
arr = np.array([int(input(f"Enter element {i+1}: ")) for i in range(n)])
x = int(input("Enter the element to be searched: "))
for i in range(n):
    if arr[i] == x:
        print("Element found at position: ", i+1)
        break
    else:    
        print("Element not found in the array")