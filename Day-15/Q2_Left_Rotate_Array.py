import numpy as np
print("Left Rotated Array")
n=int(input("Enter the number of elements in the array:"))
arr=np.array([int(input(f"Enter element {i+1}: ")) for i in range(n)])
print("Original Array:",arr)
d=int(input("Enter the number of positions to rotate:"))
left_rotated_arr=np.roll(arr, -d)
print("Left Rotated Array:", left_rotated_arr)