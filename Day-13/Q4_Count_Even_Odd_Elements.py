print("Count of Even and Odd Elements in an Array")
import numpy as np
n = int(input("Enter the number of elements in the array: "))
if n <= 0:
    print("Please enter a positive integer for the number of elements.")
    exit()
arr=np.array([int(input(f"Enter element {i+1}: ")) for i in range(n)])
even_count = np.sum(arr % 2 == 0)
odd_count = np.sum(arr % 2 != 0)
print(f"The number of even elements in the array is: {even_count}")
print(f"The number of odd elements in the array is: {odd_count}")