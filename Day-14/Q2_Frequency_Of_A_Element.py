print("Frequency of the element")
import numpy as np
n = int(input("Enter the number of elements in the array: "))
arr = np.array([int(input(f"Enter element {i+1}: ")) for i in range(n)])
x = int(input("Enter the element to find its frequency: "))
if x not in arr:
    print("Element not found in the array")
else:
    count = np.sum(arr == x)
    print(f"The frequency of {x} in the array is: {count}")