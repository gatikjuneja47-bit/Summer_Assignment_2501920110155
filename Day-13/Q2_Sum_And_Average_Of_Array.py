print("Sum and Average of an Array")
import numpy as np
n = int(input("Enter the number of elements in the array: "))
if n <= 0:
    print("Please enter a positive integer for the number of elements.")
    exit()
arr=np.array([int(input(f"Enter element {i+1}: ")) for i in range(n)])
total = np.sum(arr)
average = np.mean(arr)
print(f"The sum of the array is: {total}")
print(f"The average of the array is: {average}")