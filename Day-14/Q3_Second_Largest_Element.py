print("Second Largest Element")
import numpy as np
n = int(input("Enter the number of elements in the array: "))
arr = np.array([int(input(f"Enter element {i+1}: ")) for i in range(n)])
if n < 2:
    print("Array should have at least 2 elements")
largest = arr[0]
second_largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]
if second_largest == largest:
    print("There is no second largest element in the array")
else:    print("The second largest element in the array is: ", second_largest)