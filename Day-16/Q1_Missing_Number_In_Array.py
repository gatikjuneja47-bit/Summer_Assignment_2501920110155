print("missing number in array")
import numpy as np
n = int(input("enter the size of array: "))
arr = np.array([int(input(f"enter element {i+1}: ")) for i in range(n-1)])
arr.sort()
missing_number = 0
for i in range(1, n + 1):
    if i != arr[i - 1]:
        missing_number = i
        break
print("missing number is:", missing_number)