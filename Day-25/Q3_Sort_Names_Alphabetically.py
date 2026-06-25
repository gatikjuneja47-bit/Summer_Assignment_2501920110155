print("Sorting names alphabetically")
import numpy as np
n = int(input("Enter the number of names: "))
names = np.array([input("Enter name {}: ".format(i+1)) for i in range(n)])
names.sort()
print("Names sorted alphabetically:")
print(names)