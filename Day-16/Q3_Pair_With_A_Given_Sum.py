print("pair with given sum in array")
import numpy as np
n = int(input("enter the size of array: "))
arr = np.array([int(input(f"enter element {i+1}: ")) for i in range(n)])
sum = int(input("enter the given sum: "))
pairs = np.array([], dtype=int)
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == sum:
            pairs = np.append(pairs, (arr[i], arr[j]))

if pairs.size > 0:
    print("pairs with given sum are:", pairs)
else:
    print("no pairs found with given sum")