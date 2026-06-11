print("Selection Sort")
import numpy as np
n = int(input("Enter the number of elements: "))
arr = np.array([], dtype=int)
for i in range(n):
    arr = np.append(arr, int(input("Enter element {}: ".format(i+1))))

for i in range(n):
    min = i
    for j in range(i+1, n):
        if arr[j] < arr[min]:
            min= j
    arr[i], arr[min] = arr[min], arr[i]

print("Sorted array is:", arr)