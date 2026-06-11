print("Largest and Smallest Element in an Array")
import numpy as np
n = int(input("Enter the number of elements in the array: "))
if n <= 0:
    print("Please enter a positive integer for the number of elements.")
    exit()
arr=np.array([int(input(f"Enter element {i+1}: ")) for i in range(n)])
largest = np.max(arr)
smallest = np.min(arr)
print(f"The largest element in the array is: {largest}")
print(f"The smallest element in the array is: {smallest}")