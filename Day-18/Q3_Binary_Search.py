print("Binary Search")
import numpy as np
n = int(input("Enter the number of elements: "))
arr = np.array([], dtype=int)
for i in range(n):
    arr = np.append(arr, int(input("Enter element {}: ".format(i+1))))
arr.sort() 
print("Sorted array is:", arr)
target = int(input("Enter the element to search: "))
low = 0
high = n - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print("Element found at index:", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")