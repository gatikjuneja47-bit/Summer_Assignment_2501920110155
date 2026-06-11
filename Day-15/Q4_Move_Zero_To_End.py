print("move zero to end of the array")
import numpy as np
n=int(input("Enter the Elements of the array:"))
arr=np.array([int(input(f"Enter element {i+1}: "))for i in range(n)])
print("Original Array:", arr)
non_zero_arr=np.array([num for num in arr if num!=0], dtype=int)
zero_arr=np.array([num for num in arr if num==0], dtype=int)
result=np.append(non_zero_arr, zero_arr)
print("Array with zeros moved to the end:", result)