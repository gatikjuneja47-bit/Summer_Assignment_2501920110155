print("Right Rotated Array")
import numpy as np
n=int(input("Enter the Elements of the array:"))
arr = np.array([int(input(f"Enter elememnt {i+1}: "))for i in range(n)])
print("Original Array:", arr)
d=int(input("Enter the number of positions to rotate: "))
rotated_arr=np.roll(arr, +d)
print("Right Rotated Array:", rotated_arr)