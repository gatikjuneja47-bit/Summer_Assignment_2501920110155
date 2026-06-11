print("Interaction of two arrays")
import numpy as np
n1 = int(input("Enter the size of first array: "))
arr1 = np.array([], dtype=int)
for i in range(n1):
    arr1 = np.append(arr1, int(input("Enter element {}: ".format(i+1))))

n2 = int(input("Enter the size of second array: "))
arr2 = np.array([], dtype=int)
for i in range(n2):
    arr2 = np.append(arr2, int(input("Enter element {}: ".format(i+1))))

interaction_array = np.array([x for x in arr1 if x in arr2])
print("Interaction of arrays:", interaction_array)