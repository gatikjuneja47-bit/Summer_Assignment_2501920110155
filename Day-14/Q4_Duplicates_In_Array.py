print("Duplicates in the array")
import numpy as np
n = int(input("Enter the number of elements in the array: "))
arr = np.array([int(input(f"Enter element {i+1}: ")) for i in range(n)])
duplicates = np.array([], dtype=int)
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates = np.append(duplicates, arr[i])
if duplicates.size > 0:
    print("The duplicate elements in the array are: ", duplicates)
else:
    print("There are no duplicate elements in the array")