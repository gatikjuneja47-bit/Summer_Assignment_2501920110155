import numpy as np
print("Reversed Array")
n=int(input("Enter the number of elements in the array:"))
arr=np.array([int(input(f"Enter element {i+1}: ")) for i in range(n)])
print("Original Array:",arr)
reversed_arr=arr[::-1]
print("Reversed Array:",reversed_arr)