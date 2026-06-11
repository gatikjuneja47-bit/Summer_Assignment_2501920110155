print("Bubble Sort")
import numpy as np
n = int(input("Enter the number of elements: "))
arr = np.array([], dtype=int)
for i in range(n):
    arr = np.append(arr, int(input("Enter element {}: ".format(i+1))))
    
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array is:", arr)