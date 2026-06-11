print("maximum frequency element in array")
import numpy as np
n = int(input("enter the size of array: "))
arr = np.array([int(input(f"enter element {i+1}: ")) for i in range(n)])
frequency = {}
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_frequency = 0
max_element = None
for num, freq in frequency.items():
    if freq > max_frequency:
        max_frequency = freq
        max_element = num

print("maximum frequency element is:", max_element)