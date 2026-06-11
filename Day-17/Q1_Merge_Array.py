print("Merging two arrays")
import numpy as np
n1 = int(input("Enter the size of first array: "))
arr1 = np.array([], dtype=int)
for i in range(n1):
    arr1 = np.append(arr1, int(input("Enter element {}: ".format(i+1))))

n2 = int(input("Enter the size of second array: "))
arr2 = np.array([], dtype=int)
for i in range(n2):
    arr2 = np.append(arr2, int(input("Enter element {}: ".format(i+1))))

merged_array = np.concatenate((arr1, arr2))
print("Merged array:", merged_array)